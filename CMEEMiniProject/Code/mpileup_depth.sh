#! /usr/bin/bash

''' 
Script that converts an mpileup file into depth files
Takes 2 inputs:
    First input - the name of the mpileup file including path to file
    Second input - number of samples within the mpileup file
Outputs a seperate depth file for each of the samples present in the mpileup file

Example use from terminal: 
    bash mpileup_depth.sh ../Data/example_mpileup 5

    Resulting files would be ../Data/example_mpileup_i.txt for i=1,2,3,4,5
'''

NSAMS=$2


for i in `seq 1 $NSAMS`;
    do
        echo Extracting sample ${i}
        cut -f $((4+((i-1)*3))) $1 > $1_depth_sample_${i}.txt  # extracts the depth data from the 

        # Rscript -e "vals=as.numeric(readLines('$1_depth_sample_${i}.txt'));pdf(file='$1_depth_sample_${i}.pdf');hist(vals, breaks=50);dev.off()" # # produces pdf of dpeth data

        # evince $1_depth_sample_${i}.pdf # open plot of depth
    done






