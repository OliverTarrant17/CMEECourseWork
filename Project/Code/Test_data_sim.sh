
#### Requires R package, getopt
POLY=../Code/ngsJulia/ngsPoly

NSAMS=$4    # Number of samples
MEANDEPTH=$1 # Mean read depth of the sample
COPIES=$2
number=$3
NSITES=10000 # Numer of sites measured
output=../Data/Data_sims/$3_T${COPIES}.mpileup
	

offset=0 
for MEANDEPTH in $MEANDEPTH
do
	

	for i in `seq 1 1`;     # Specify the number of chromosomes
        
	do                  # For each chromosome .....
        > $output      # Create a results file
		ERR=$(python -c "import random;print(round(random.uniform(0.2, 0.4),3))")

		echo $i            # Write the number of the chromosome currently being calculated
		CHROMDEPTH=${MEANDEPTH}        # Calculate the mean depth expected for this chromosome (mean depth*ploidy of the chromosome)

	    Rscript $POLY/simulMpileup.R --copy $COPIES --sites $NSITES --depth $CHROMDEPTH --offset $offset --errdepth $ERR --inbred 0.0x${NSAMS}  >> $output
        gzip $output
	    

	done

done