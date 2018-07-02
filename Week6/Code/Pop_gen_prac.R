library(dplyr)
library(ggplot2)
library(reshape2)
g <- read.table(file = "../Data/General_Data/H938_chr15.geno", header=TRUE)
head(g)
dim(g)
#### There are 19560 snps ###
g <- mutate(g, nObs= nA1A1 + nA1A2 + nA2A2)
head(g)
summary(g$nObs)
qplot(nObs, data = g, bins = 20)
### most do have complete data as both 1st Qu. all the way up to Max are 938 
### so atleast 75% have full data
### Lowest count observed is 887 this is 94.5% 
# compute genotype frequencies
g <- mutate(g, p11 = nA1A1/nObs, p12 = nA1A2/nObs, p22 = nA2A2/nObs)
# Compute allele frequencies from genotype frequencies
g <- mutate(g, p1 = p11+0.5*p12, p2=p22+0.5*p12)
# plot frequency of A2 vs frequency of A1
qplot(p1, p2, data = g)
### equation of relationship p2 = 1 - p1 
### note p1+p2 must sum to 1

## Plot genotype vs allele frequencies
gTidy <- select(g, c(p1,p11,p12,p22)) %>%
  melt(id='p1', value.name = "Genotype.Proportion")
# seclect subsets data on columns we want then pass to melt
# to reformat it
head(gTidy)
dim(gTidy)
ggplot(gTidy) + geom_point(aes(x = p1, y = Genotype.Proportion, 
                               color = variable, shape = variable))
### plot looks like HWE 
### p11 ~ p1^2
### p12 ~ 2p1(1-p1)
### p22 ~ (1-p1)^2
# add in HWE lines
ggplot(gTidy) +geom_point(aes(x=p1, y = Genotype.Proportion,
                             color = variable, shape = variable)) +
  stat_function(fun=function(p) p^2, geom = "line", color = "red",
                size = 2.5) + stat_function(fun=function(p) 2*p*(1-p),
                                            geom = "line", colour = "green",
                                            size = 2.5) + stat_function(
                                              fun = function(p) (1-p)^2,
                                              geom="line", colour = "blue",
                                              size = 2.5)
## systematic deficiency of heterozygots and excess of homozygotes
## This is probably due to population structure

####### Testing Hardy Weinberg ########
# pearsons chi squared test
# there is 1DF 
g <- mutate(g, X2 = (nA1A1-nObs*p1^2)^2/(nObs*p1^2) + 
              (nA1A2 - nObs * 2 * p1 * p2)^2/(nObs * 2 * p1 * p2) +
              (nA2A2 - nObs * p2^2)^2/(nObs*p2^2))
g <- mutate(g, pval = 1 - pchisq(X2,1))
head(g$pval)
# p- value gives srequency at which observed departure from expectations 
# or more extreme departure would occur if the null hypothesis is true. 
# generally reject null if p < 0.05 and keep otherwise
# note problem as if 50000 SNPS all obeyign the null then would on average
# reject the null nievely in ~2500
sum(g$pval < 0.05, na.rm = TRUE)
# 14314 below 0.05
# more than would be expected if HWE was true so looking like not a 
# good statistical fit
qplot(pval, data = g)
# if distributed under the null the pvalues should be approximately
# uniformly distributed
# our data is very positivly skewed suggesting systematic departure from HWE
# quick plot of expected vs observed heterozygosity
qplot(2*p1*(1-p1),p12, data = g) + geom_abline(intercept = 0, slope = 1,
                                               color = "red", size = 1.5)
# note most points below the y = x line (deficiency in heterozygotes)

## The correlation of uniting gametes:
# A1A1 individual requires A1 egg and A1 sperm, expect at rate p1^2
# but if correlated so that A egg is more likely to join with an A sperm 
# then more A1A1 that 2p1^2 and fewer A1A2 than 2p1p2
### As our data is from 52 subpopulations, and alleles have probability of 
### clustering in populations, a good hypothesis for deficiency of heterozygotes
### is the presence of population structure (non random mating)
### note seems statistically significant but not too wildly (by plot)
## Average deficiency of heterozygotes 
g <- mutate(g, hetro.def = (2*p1*(1-p1)-p12)/(2*p1*(1-p1)))
mean(g$hetro.def)
g$hetro.def <- NULL
head(g)
# average heterozygosity deficiency is 0.1102838
# rule of thumb is approx 10% in human global population 
# Human populations are not very deeply structured
# most alleles in this sample are globally widespread and not suficiently 
# geographically clustered to generate correlations amoung the uniting alleles
# This is as humans developed from an original popualtion only 100-150 
# thousand years ago (small time to develop genetic variation)

###### Finding specific loci that are large departures from Hardy Weinberg #####
# Want to find deficiency per SNP. This number is reffered to as F
# and has connectiosn to correlation coefficients 
# If we assume there is no inbreeding within populations then 
# this number is an estimate of F_ST
# adding this number to the dataframe 
g <- mutate(g, F = (2*p1*(1-p1)-p12)/(2*p1*(1-p1)))
# plot the results
plot(g$F, xlab = "SNP number", ylab = "F value")
# When a high/low F value is due to genotyping error then likely only affects 
# a single SNP. However, when some population genetic force acting on the region 
# of the genome, likely that it'll affect multiple SNPs in the region.
# Want a local average in a sliding window of SNPs across the genome
# computing an average F over every 5 consecutive SNPs.
# stats::filter calls filter frim stats library
movingavg <- function(x,n=5){stats::filter(x, rep(1/n,n), sides = 2)}
# function takes 5 values centered on a focal SNP
# gives each weigth 1/5 then takes sum to produce the local average
# plot the moving average
plot(movingavg(g$F), xlab = "SNP number")
# look at largest spike
outlier = which(movingavg(g$F) == max(movingavg(g$F), na.rm = TRUE))
g[outlier,]
# outlier is SNP rs12440301
# nearest gene is SEMA6D
# It is thought high F value here is because natural selection led to a 
# geographic clustering of alleles in these gene region
# increasing the window size absorbs the larger peaks and reduces the averages
# decreasing it makes them more prominant and the graph less smooth
