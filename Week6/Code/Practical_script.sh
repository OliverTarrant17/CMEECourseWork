#! /bin/bash
### Working through practical 3 worksheet.

### Open the plink data sets and explore the data

### number of samples (lines in ME_Dataset1.fam)

wc -l ../Data/General_Data/Dataset1/ME_Dataset1.fam
# answer = 69


### Number of SNPs in the data (lines in ME_Dataset1.bim)

wc -l ../Data/General_Data/Dataset1/ME_Dataset1.bim
# answer 158487

### Check if expected number of heterozygotes given Harfy Weinburg
### expectations
## Count the number of each genotype using plink

plink --bfile ../Data/General_Data/Dataset1/ME_Dataset1 --freqx --out ../Results/ME_DatasetA
# 4. remove unwanted output files
rm ../Results/ME_DatasetA.nosex
# 5. inspect the genotype counts
head ../Results/ME_DatasetA.frqx
# 6. Convert .frqx file to .geno file
./frqx2geno.pl ../Results/ME_DatasetA.frqx ../Results/ME_DatasetA.geno
# 7. Plot the observed vs expected genotype frequecies
./Ob_v_Ex_het.R ../Data/General_Data/H938_chr15.geno ../Results/ME_DatasetA_ObvEx_het_myVers.pdf
# most points are above the line this suggests higher number of heterozygotes
# than at Hardy Weinburg 

# 8. Plot moving F-vaues for the dataset
./Moving_F.R ../Results/ME_DatasetA.geno ../Results/ME_DatasetA_F.pdf
# There are no major outlier regions

# 9. Test for HWE on each SNP using the exact test
plink --bfile ../Data/General_Data/Dataset1/ME_Dataset1 --hardy --out ../Results/ME_Dataset1HW

# 10. Inspect outputted file
head ../Results/ME_Dataset1HW.hwe
# gives observed and expected heterozygosity for each SNP along with associated p value

# 11. Find 50 SNPs with greatest departure from HWE (do by sorting by p value)
sort -k9 ../Results/ME_Dataset1HW.hwe | tail -n 50
# -k9 says to sort by the 9th column of the data set from greatest to smallest

# 12. Save these lines as a file of outliers
sort -k9 ../Results/ME_Dataset1HW.hwe | tail -n 50 >../Results/ME_Dataset1_HWE_outliers.txt


