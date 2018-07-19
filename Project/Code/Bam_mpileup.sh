#! /usr/bin/bash
#### Code to generate a mpileup file from a list of input BAM files #####

REF=../Data/Cryptococcus/Cng_h99_CNA3_suprcont.fasta # Reference genome in fasta format
CHR=14 # number of supercontigs
echo "Reference genome is ${REF}"
BAMLIST='../Data/Cryptococcus/VN1/*.bam' # All bam files
> ../Data/Cryptococcus/VN1/bamlist.txt # Create a blank text file to add bam file names to
for bam in $BAMLIST
    do 
        echo "${bam} found"
        samtools index ${bam} # Create indexed bam files
        echo ${bam} >> ../Data/Cryptococcus/VN1/bamlist.txt # Create a list of the bam files to be fed into samtools
        echo "${bam} added"
    done

NSAMS=`wc -l < ../Data/Cryptococcus/VN1/bamlist.txt` # Calculate number of sampels from the number of files in the bamlist
for i in `seq 1 ${CHR}`
    do
        samtools mpileup -f ${REF} -r Supercontig_3.${i} -b ../Data/Cryptococcus/VN1/bamlist.txt -C 50 -q 20 -Q 20 -E -d 200 > ../Data/Cryptococcus/VN1/Supercontig_3.${i}.mpileup
        echo `wc -l < ../Data/Cryptococcus/VN1/Supercontig_3.${i}.mpileup`
    done
i=0
rm ../Data/Cryptococcus/VN1/bamlist.txt
> ../Data/Cryptococcus/VN1/bamlist.txt
for bam in $BAMLIST
    do
        i=$((i+1))
        temp=${bam##*/} # remove path
        temp=${temp%.*} # remove .bam
        echo ${temp} >> ../Data/Cryptococcus/VN1/bamlist.txt
        #### For depth file generation
        #echo "Generating depth file for sample ${temp}" 
        #cut -f $((4+((i-1)*3))) ../Data/Cryptococcus/mpileup > ../Data/Cryptococcus/Depths/${temp}_depth.txt # extract depth from mpileup
        #echo "${temp}_depth.txt created"
        
    done
