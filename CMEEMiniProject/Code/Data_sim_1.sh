
#### Requires R package, getopt
POLY=../Code/ngsPoly

NSAMS=1    # Number of samples
MEANDEPTH='2 5 10 25 50 100' # Mean read depth of the sample
NSITES=10000 # Numer of sites measured

offset=0 
for MEANDEPTH in $MEANDEPTH
do
	> ../Data/First_Analysis/$MEANDEPTH/try.mpileup       # Create a results file

	for i in `seq 1 5`;     # Specify the number of chromosomes
	do                  # For each chromosome .....

		echo $i            # Write the number of the chromosome currently being calculated
		CHROMDEPTH=$((MEANDEPTH*i))        # Calculate the mean depth expected for this chromosome (mean depth*ploidy of the chromosome)

		Rscript $POLY/simulMpileup.R --copy ${i}x${NSAMS} --sites $NSITES --depth $CHROMDEPTH --offset $offset --errdepth 0.05 --seed ${MEANDEPTH} >> ../Data/First_Analysis/$MEANDEPTH/try.mpileup

		offset=$((offset+NSITES))

	done

	cut -f 4 ../Data/First_Analysis/$MEANDEPTH/try.mpileup > ../Data/First_Analysis/$MEANDEPTH/depth.txt

	Rscript -e "vals=as.numeric(readLines('../Data/First_Analysis/$MEANDEPTH/depth.txt'));pdf(file='../Data/First_Analysis/$MEANDEPTH/depth.pdf');hist(vals, breaks=50);dev.off()"


	#evince ../Data/First_Analysis/$MEANDEPTH/depth.pdf
done




