#! usr/bin/python3
import sys
import gzip
import generics
import numpy as np
import math 
import scipy.stats
import random
from statistics import mode
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("input",help="file containing the list of basenames for gzipped mpileup files for use in analysis to be used")
parser.add_argument("-w","--window",type=int,help="Set the window size for genotype likelihood windows. Must match the value used in Genotype_Likelihood script (reccomended approximately 1/10 of number of SNPs", default=50)
args = parser.parse_args()

ploidy=[1,2,3,4,5,6,7,8]
alleles = ['A','C','G','T']
samples_included=[]



input = args.input #Input file in form of gziped mpileup
list_of_inputs=[]
samples=[]
with open("../Data/Cryptococcus/bamlist.txt",'rt') as sams:
    for line in sams:
        samples.append(line.split(".")[0])
NSAMS=len(samples)
with open(input,'rb') as f:# opens the mpilup. Use mpileup.read() to display content
    for line in f:
        line=line.decode().strip('\n')# Convert bytes into string
        sample_name=line
        line=line+".mpileup.gz"
        list_of_inputs.append(line)
Nfiles=len(list_of_inputs)
print('%d files found' %Nfiles)
print(list_of_inputs)

Ovr_total_snps=[0 for sample in range(NSAMS)]
Ovr_number_of_reads=[0 for sample in range(NSAMS)]
Ovr_ploidies=[[0 for ploid in ploidy] for sample in range(NSAMS)]
Ovr_bases=0
chrom_stats=""


for g in list_of_inputs:
    directory = '/'.join(g.split('/')[:-1])
    if directory =='':
        directory="."
    g = g.split('/')[-1]
    basename='.'.join(g.split('.')[:-2]) # Extract name of file for saving results, -2 to remove .mpileup.gz
    output = basename+".genolikes.gz" # output file to contain genotype likelihoods
    mpileup= basename+".mpileup.gz"
    output_2 = basename+".stats" # output file to contain inferred ploidies and whether aneuploidy or not
    open(directory+'/'+output_2,'wt')#create stats file
    with gzip.open(directory+'/'+g) as f:
        first_line = f.readline()
        Data=first_line.decode().strip('\n')# Convert bytes into string
        l = Data.split('\t')
    NSAMS=int((len(l)-3)/3)
    

    
    bases=0 #chromosome length
    with gzip.open(directory+'/'+mpileup) as mp:
        for line in mp:
            bases+=1
            Ovr_bases+=1
    


    snps=0
    total_snps=[0 for sample in range(NSAMS)]
    number_of_reads=[0 for sample in range(NSAMS)]
    ploidies=[[0 for ploid in ploidy] for sample in range(NSAMS)]

    base_number=0
    total_bases=0
    with gzip.open(directory+'/'+output) as genos:
        for line in genos:
            snps+=1
            Data=line.decode().strip('\n')# Convert bytes into string
            l = Data.split('\t')
            sampleDepth=int(l[4])
            sample_number=int(l[2]) # sample number
            if sampleDepth>0:
                total_snps[sample_number-1]+=1
                Ovr_total_snps[sample_number-1]+=1
                number_of_reads[sample_number-1]+=sampleDepth
                Ovr_number_of_reads[sample_number-1]+=sampleDepth
                #calculate number of bases at each ploidy level
                p=[]
                if 1 in ploidy:
                    haploid = l[9:11]
                    haploid_sum = generics.log_or_zero(sum(map(lambda x:generics.exp_or_zero(float(x)),haploid)))
                    p.append(haploid_sum)
                if 2 in ploidy:
                    diploid = l[11:14]
                    diploid_sum = generics.log_or_zero(sum(map(lambda x:generics.exp_or_zero(float(x)),diploid)))
                    p.append(diploid_sum)
                if 3 in ploidy:
                    triploid = l[14:18]
                    triploid_sum = generics.log_or_zero(sum(map(lambda x:generics.exp_or_zero(float(x)),triploid)))
                    p.append(triploid_sum)
                if 4 in ploidy:
                    tetraploid = l[18:23]
                    tetraploid_sum = generics.log_or_zero(sum(map(lambda x:generics.exp_or_zero(float(x)),tetraploid)))
                    p.append(tetraploid_sum)
                if 5 in ploidy:
                    pentaploid = l[23:29]
                    pentaploid_sum = generics.log_or_zero(sum(map(lambda x:generics.exp_or_zero(float(x)),pentaploid)))
                    p.append(pentaploid_sum)
                if 6 in ploidy:
                    hexaploid = l[29:36]
                    hexaploid_sum = generics.log_or_zero(sum(map(lambda x:generics.exp_or_zero(float(x)),hexaploid)))
                    p.append(hexaploid_sum)
                if 7 in ploidy:
                    heptaploid = l[36:44]
                    heptaploid_sum = generics.log_or_zero(sum(map(lambda x:generics.exp_or_zero(float(x)),heptaploid)))
                    p.append(heptaploid_sum)
                if 8 in ploidy:
                    octaploid = l[44:53]
                    octaploid_sum = generics.log_or_zero(sum(map(lambda x:generics.exp_or_zero(float(x)),octaploid)))
                    p.append(octaploid_sum)
                ploidies[sample_number-1][p.index(max(p))]+=1
                Ovr_ploidies[sample_number-1][p.index(max(p))]+=1
    
   
    c_stats=(str(bases),str(snps))
    c_stats="\t".join(c_stats)+"\n"
    chrom_stats=chrom_stats+c_stats
    stats=""
    for i in range(NSAMS):
        to_print=(str(samples[i]),str(bases),str(total_snps[i]),str(number_of_reads[i]),"\t".join(map(str,ploidies[i])))
        to_print="\t".join(to_print)+"\n"
        stats=stats+to_print
    stats=stats.strip("\n")
    with open(directory+'/'+output_2,'at+') as f: 
        f.write(stats)
    print("file_{} done".format(g))
Ovr_stats=""
with open(directory+'/Chromosome.stats','at+') as f: 
    f.write(chrom_stats)
for j in range(NSAMS):
    Ovr_to_print=(str(samples[i]),str(Ovr_bases),str(Ovr_total_snps[i]),str(Ovr_number_of_reads[i]),"\t".join(map(str,Ovr_ploidies[i])))
    Ovr_to_print="\t".join(Ovr_to_print)+"\n"
    Ovr_stats=Ovr_stats+Ovr_to_print
with open(directory+'/Overall.stats','at+') as f: 
    f.write(stats)
print("file_Overall_{} done".format(g))
                
                

    

