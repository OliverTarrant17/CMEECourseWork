#~ #!/usr/bin/Rscript


#~ #A script that outputs a .pdf plot of the moving average F value.
#~ ##Written by: Udita Bansal udita.bansal17@imperial.ac.uk
#~ #Written on: 8/11/2017



#~ #remove all existing lists    HIS IS AN UNECESSARY STEP FOR A STANDALONE SCRIPT SINCE NONE WILL EXIST UNLESS YOU HAVE CREATED THEM IN THE SCRIPT
#~ #rm(list=ls())

#~ #install package dplyr and ggplot2    NEVER INSTALL PACKAGES IN A REUSABLE SCRIPT BECAUSE YOU WILL END UP REINSTALLING THE SAME PACKAGE OVER AND OVER AGAN.
#~ #install.packages("dplyr")
#~ #install.packages("ggplot2")

#~ #call for the installed packages
#~ library(dplyr)
#~ library(ggplot2)

#~ #assign the commandArgs function to cargs
#~ cargs<- commandArgs(T)

#~ #get infile from command line
#~ infile<- cargs[1]

#~ #assign output file name using command line
#~ outfile<- cargs[2]

#~ #load data
#~ g <- read.table(file=infile, header=TRUE)

#~ #add up number of observatuons in last three columns and create a new column with the sum
#~ g<- mutate(g, nObs= nA1A1 + nA1A2 + nA2A2)

#~ #Compute observed genotype frequencies
#~ g <- mutate(g, p11 = nA1A1/nObs , p12 = nA1A2/nObs, p22 = nA2A2/nObs ) 

#~ #Compute allele frequencies (using Hardy Weinberg rule) from genotype frequencies
#~ g <- mutate(g, p1 = p11 + 0.5*p12, p2 = p22 + 0.5*p12)

#~ #compute F value and add it to the data table
#~ g <- mutate(g, F = (2*p1*(1-p1)-p12) / (2*p1*(1-p1))) 

#~ #compute moving average
#~ movingavg <- function(x, n=5){stats::filter(x, rep(1/n,n), sides = 2)} 

#~ #plot a graph for moving average and save it as pdf in the current working directory
#~ pdf(outfile, 11.7, 8.3)       # YOU HAD OUTFILE IN QUOTES HERE WHICH NAMED THE FILES ALL "outfile"
#~ plot(movingavg(g$F), xlab="SNP number")
