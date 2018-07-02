#! /usr/bin/Rscript
### A script that outputs a plot of the observed
### versus expected heterozygoscity as a pdf file
library(dplyr)
library(ggplot2)
library(reshape2)
library(tools)
# check correct command line arguments are added
cargs <- commandArgs(T)
if(length(cargs)<2) stop("Not enough arguents")
if(length(cargs)>2) stop("Too many arguments")

infile <- cargs[1] # input data file name
outfile <- cargs[2] # output data file name
outfile <- tools::file_path_sans_ext(outfile) # strip file extension


g <- read.table(file = infile, header=TRUE)
#### There are 19560 snps ###
g <- mutate(g, nObs= nA1A1 + nA1A2 + nA2A2) # add observation no.
# add genotype frequencies
g <- mutate(g, p11 = nA1A1/nObs, p12 = nA1A2/nObs, p22 = nA2A2/nObs)
# Compute allele frequencies from genotype frequencies
g <- mutate(g, p1 = p11+0.5*p12, p2=p22+0.5*p12)

# plot of expected vs observed heterozygosity
p <- ggplot(g) + geom_point(aes(x=2*p1*(1-p1), y = p12),color = "blue")
p <- p + scale_x_continuous(name = "Observed heterozygosity") +
  scale_y_continuous(name = "Expected heterozygosity") + 
  ggtitle("Plot of observed vs expected heterozygosity") +
  geom_abline(intercept = 0, slope = 1, color = "red", size = 1.5)

#print graph to pdf
pdf(file = paste("../Results/", outfile, ".pdf"), 11.7, 8.3)
print(p)
dev.off()
