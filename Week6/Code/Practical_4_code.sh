###### Code for bioinformatics pracical 4 #####
# Have a look at the data
cat ../Data/General_Data/mutant_R1.fastq | less
# Assess the quality of the data
fastqc --nogroup ../Data/General_Data/mutant_R1.fastq ../Data/General_Data/mutant_R2.fastq
#firefox mutant_R1_fastqc.html &
# Sequence quality is pretty good

### Removing low quality bases
skewer --help
skewer -m pe -q 30 -Q 35 -l 75 -z -o ../Results/mutant ../Data/General_Data/mutant_R1.fastq ../Data/General_Data/mutant_R2.fastq


## Kmer counting - a way of estimating assembly coverage 
# (the average number of reads which align under each assembled nucleotide)
#kmercountexact.sh in1=../Results/mutant-trimmed-pair1.fastq.gz in2=../Results/mutant-trimmed-pair2.fastq.gz khist=../Results/trimmed.khist
# plot results
##Rscript ~/software/plot_kmer.R ../Results/trimmed.khist
###eog ../Results/kmercov.png

############Genome assembly ##########
### Using Spades assembly
#spades.py -o ../Results/mutant_assembly --careful -1 ../Results/mutant-trimmed-pair1.fastq.gz -2 ../Results/mutant-trimmed-pair2.fastq.gz
#less ../Results/mutant_assembly/scaffolds.fasta
#quast.py ../Results/wildtype.fna ../Results/mutant_assembly/scaffolds.fasta
#firefox quast_results/latest/report.html &

##### Annotating the new mutant genome
#prokka ../Results/mutant_assembly/scaffolds.fasta
### Count the protein sequences
# grep -c ">" PROKKA_{DATE}/PROKKA_11092017.faa

### Map the reads from the mutants to tghe wildtypes
## Creates an index file
# bwa index wildtype.fna
##Maps the mutant reads to the wildtype genome 
# bwa mem wildtype.fna ../Results/mutant-trimmed-pair1.fastq.gz ../Results/mutant-trimmed-pair2.fastq.gz > ../Results/mutant.vs.wildtype.sam
# samtools sort -@ 2 -0 bam -T temp_${RANDOM} ../Results/mutant.vs.wildtype.sam > mutant.vs.wildtype.bam

## Find the variant sites
# freebayes -f wildtype.fna -p 1 ../Results/mutant.vs.wildtype.bam > ../Results/mutant.vs.wildtype.bam.vcf
## Summaris the file
# vcfstats ../Results/mutant.vs.wildtype.bam.vcf


