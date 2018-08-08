rm(list=ls())
graphics.off()
library(ggplot2)
library(RColorBrewer)

args = commandArgs(trailingOnly=TRUE)
input="../Data/Cryptococcus/Chromosome.stats"
stats=read.csv(input,sep="\t",header=FALSE) # load the stats
correction=sum(1/c(1:23))
stats$theta<-(stats$V2)/correction

