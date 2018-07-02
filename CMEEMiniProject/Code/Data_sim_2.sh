#! /bin/bash

#### Requires R package, getopt
### Seed used in R generation of 42
POLY=../Code/ngsPoly

NSAMS=1    # Number of samples
MEANDEPTH='2 5 10 25 50 100' # Mean read depth of the sample
NSITES=10000 # Numer of sites measured

offset=0 
for MEANDEPTH in $MEANDEPTH
do
    for j in `seq 1 500`;
    do
        k=$((((j-1)/100)+1))
        echo Depth $MEANDEPTH Genome $j

        > ../Data/Second_Analysis/${MEANDEPTH}/try.mpileup_mix_${j}       # Create a Data file
      
        for i in `seq 1 $k`;     # Specify the number of chromosomes
        do                  # For each chromosome .....
        

    	    echo $i            # Write the number of the chromosome currently being calculated
    
            CHROMDEPTH=$((MEANDEPTH*i))
        	Rscript $POLY/simulMpileup.R --copy ${i}x${NSAMS} --sites $NSITES --depth $CHROMDEPTH --offset $offset --errdepth 0.05 --seed ${j} >> ../Data/Second_Analysis/${MEANDEPTH}/try.mpileup_mix_${j}

        	offset=$((offset+NSITES))
    
        done


        cut -f 4 ../Data/Second_Analysis/${MEANDEPTH}/try.mpileup_mix_${j} > ../Data/Second_Analysis/${MEANDEPTH}/mix_depth_${j}.txt

        Rscript -e "vals=as.numeric(readLines('../Data/Second_Analysis/${MEANDEPTH}/mix_depth_${j}.txt'));pdf(file='../Data/Second_Analysis/${MEANDEPTH}/mix_depth_${j}.pdf');hist(vals, breaks=50);dev.off()"

    done
done