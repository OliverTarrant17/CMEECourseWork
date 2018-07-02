
#### Requires R package, getopt
POLY=../Code/ngsJulia/ngsPoly

NSAMS=$3   # Number of samples
MEANDEPTH=$1 # Mean read depth of the sample
COPIES=$2
NSITES=10000 # Numer of sites measured
output=../Data/Tests/T${COPIES}.mpileup
	

offset=0 
for MEANDEPTH in $MEANDEPTH
do
	

	for i in `seq 1 1`;     # Specify the number of chromosomes
        
	do                  # For each chromosome .....
        > $output      # Create a results file
		echo $i            # Write the number of the chromosome currently being calculated
		CHROMDEPTH=${MEANDEPTH}        # Calculate the mean depth expected for this chromosome (mean depth*ploidy of the chromosome)

	    Rscript $POLY/simulMpileup.R --copy $COPIES --sites $NSITES --depth $CHROMDEPTH --offset $offset --errdepth 0.4 --inbred 0.0x${NSAMS}  >> $output
        gzip $output
	    

	done

done