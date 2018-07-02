#! /usr/bin/Rscript
### A script that outputs pdf plot of the moving average F value
rm(list = ls())
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


# read data
g <- read.table(file = infile, header=TRUE)
# add observation no.
g <- mutate(g, nObs= nA1A1 + nA1A2 + nA2A2) 
# add genotype frequencies
g <- mutate(g, p11 = nA1A1/nObs, p12 = nA1A2/nObs, p22 = nA2A2/nObs)
# Compute allele frequencies from genotype frequencies
g <- mutate(g, p1 = p11+0.5*p12, p2=p22+0.5*p12)
# Calculate F value for each SNP
g <- mutate(g, F = (2*p1*(1-p1)-p12)/(2*p1*(1-p1)))
# computing an average F over every 5 consecutive SNPs.
# stats::filter calls filter frim stats library
movingavg <- function(x,n=5){stats::filter(x, rep(1/n,n), sides = 2)}
# function takes 5 values centered on a focal SNP
# gives each weigth 1/5 then takes sum to produce the local average
# plot the moving average



#print graph to pdf
pdf(file = paste("../Results/", outfile, ".pdf"), 11.7, 8.3)
plot(movingavg(g$F), xlab = "SNP number", ylab = "Moving Average", 
          main = "Plot of the moving average for 5 values of the F value for each SNP",
          col = "Purple")
dev.off()
