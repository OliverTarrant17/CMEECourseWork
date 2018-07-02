#! /usr/bin/bash

''' 
Script that converts an mpileup file into depth files
Takes 2 inputs:
    First input - the name of the mpileup file including path to file
    Second input - A list of samples in the order they appear in the mpileup
Outputs a seperate depth file for each of the samples present in the mpileup file

Example use from terminal: 
    bash mpileup_depth.sh ../Data/example_mpileup 5

    bash mpileup_depth.sh ../Data/Cryptococcus/Supercontig_3.1.mpileup ../Data/Cryptococcus/bamlist.txt


    Resulting files would be ../Data/example_mpileup_i.txt for i=1,2,3,4,5

    $1 is inputted mpileup file to be converted
'''
#BAMLIST=$2
NSAMS=`wc -l < ${2}`
####temporary fix for line code, try to remove to generalise more
BAMLIST='../Data/Cryptococcus/*.bam' # All bam files


j=0
for bam in $BAMLIST;
    do
        j=$((j+1))
        #temp="sed '${i}q;d' ${2}"
        temp=${bam##*/} # remove path
        temp=${temp%.*} # remove .bam
        
        echo Extracting sample ${temp}
        

        cut -f $((4+((j-1)*3))) $1 > $1_depth_${temp}.txt  # extracts the depth data from the mpileup and name the resulting depth file with the sample name

        Rscript -e "vals=as.numeric(readLines('$1_depth_${temp}.txt'));pdf(file='$1_depth_${temp}.pdf');hist(vals, breaks=50);dev.off()" # # produces pdf of dpeth data

        #evince $1_depth_${temp}.pdf # open plot of depth
    done






