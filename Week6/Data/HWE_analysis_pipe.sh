#!/bin/bash


# usage: ./Analysis.sh [PLINKIN] [outfile_prefix]



PLINK=$1    # Plink file set indicated by the user
OUT=$2      # outfile prefix indicated by the user


# the following are the necessary file names needed for the various steps

DIR=$OUT"_results"  #this is the name of the results directory
FRQX=$OUT".frqx"    # name of the .frqx file
GENO=$OUT".geno"    # name of the .geno file
OVE=$OUT"_Ob_v_Ex_het.pdf"   #name of the observed v expected heterzygosity plot
					           # name of the moving F plot
					           # name of the .hwe file
							   # name of the file containing the 50 most extreme SNPs



# Make a results directory 


mkdir $DIR


# give the commands for running the analyses exactly as you would on the terminal,
# however you should replace the file names with the appropriate variables


plink --bfile $PLINK --freqx --out $OUT   	#run plink to calculate genotype proportions


./scripts/frqx2geno.pl $FRQX $GENO   		#convert the plink output to .geno format


									    	# plot the observed versus expected heterozygosity


								     		# plot the moving F values

							
								    		# run Hardy Weinberg analysis


							       			# command to write the 50 most extreme SNPs to file



# Move everything into the results directory

mv $FRQX $DIR     	# move the .frqx file to results
mv $GENO $DIR     	# move the .geno file to results
mv $OVE $DIR		# move the observed v expected plot to results
 					# move the moving F plot to results
 					# move the .hwe file to results
 					# move the 50 SNPs file to results



mv $OUT".log" $DIR  # also move the plink log file to results. This is the record of what you have done


# cleanup 
 
rm $OUT.nosex  #get rid of unnecessary files



