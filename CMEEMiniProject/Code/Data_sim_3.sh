#! /bin/bash

#### Requires R package, getopt
POLY=../Code/ngsPoly

NSAMS=1    # Number of samples
MEANDEPTH='2 5 10 25 50 100' # Mean read depth of the sample
NSITES=10000 # Numer of sites measured
RANDOM=1 # set Random number seed

offset=0 
for MEANDEPTH in $MEANDEPTH
do
    for j in `seq 1 100`;
    do
        
        echo Depth $MEANDEPTH Genome $j

        > ../Data/Third_Analysis/${MEANDEPTH}/try.mpileup_mix_${j}       # Create a Data file
        > ../Data/Third_Analysis/${MEANDEPTH}/Genome_ploidy_${j}.txt
        for i in `seq 1 5`;     # Specify the number of chromosomes
        do                  # For each chromosome .....
        
            A=$(((RANDOM%5)+1)) # choose ploidy of chromosome
    	    echo $i            # Write the number of the chromosome currently being calculated
    	    CHROMDEPTH=$((MEANDEPTH*A))        # Calculate the mean depth expected for this chromosome (mean depth*ploidy of the chromosome)
        	Rscript $POLY/simulMpileup.R --copy ${i}x${NSAMS} --sites $NSITES --depth $CHROMDEPTH --offset $offset --errdepth 0.05 --seed ${j} >> ../Data/Third_Analysis/${MEANDEPTH}/try.mpileup_mix_${j}

        	offset=$((offset+NSITES))
            echo $A >> ../Data/Third_Analysis/${MEANDEPTH}/Genome_ploidy_${j}.txt
        done


        cut -f 4 ../Data/Third_Analysis/${MEANDEPTH}/try.mpileup_mix_${j} > ../Data/Third_Analysis/${MEANDEPTH}/mix_depth_${j}.txt

        Rscript -e "vals=as.numeric(readLines('../Data/Third_Analysis/${MEANDEPTH}/mix_depth_${j}.txt'));pdf(file='../Data/Third_Analysis/${MEANDEPTH}/mix_depth_${j}.pdf');hist(vals, breaks=50);dev.off()"

    done
done