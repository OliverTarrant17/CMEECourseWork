# usr/bin/python3

import subprocess
import os # both for subprocessing tasks
print("Starting miniproject")

'''
### Produce all the simulated data for the project
print("Producing data for single ploidy genomes")
Data_1 = os.system("bash Data_sim_1.sh")
if Data_1==0:
	print("Data_1 produced successfully")
else: 
	print("Data_1 not produced successfully")

print("Producing data for genomes with stepped levels of CCNV")
Data_2 = os.system("bash Data_sim_2.sh")
if Data_2==0:
	print("Stepped data produced successfully")
else: 
	print("Stepped data not produced successfully")

print("Producing data with random mixed ploidies")
Data_3 = os.system("bash Data_sim_3.sh")
if Data_3==0:
	print("Random ploidies data produced successfully")
else: 
	print("Random ploidies data not produced successfully")


print("All data produced")
print("Fitting models")
import Choose_Model
print("Constant ploidy models fitted")
import Mixed_Fit
print("Stepped ploidy models fitted")
import Mixed_Fit_2
print("Random ploidy models fitted")

'''


print("Starting analysis of results")

print("Analysing constant ploidies models")
First_Analysis=subprocess.Popen("/usr/lib/R/bin/Rscript --verbose First_Analysis.R",shell=True).wait()
# Check if First analysis ran successfully
if First_Analysis==0:
	print("First Analysis ran successfully")
else: 
	print("First Analysis did not ran successfully") 


print("Analysing mixed ploidies models")
Mixed_Analysis=subprocess.Popen("/usr/lib/R/bin/Rscript --verbose Confusion_Matrix_Compare.R",shell=True).wait()
# Check if mixed ploidy analysis ran successfully
if First_Analysis==0:
	print("Mixed Analysis ran successfully")
else: 
	print("Mixed Analysis did not ran successfully")


print("Analysing random ploidies data")
Random_Analysis=subprocess.Popen("/usr/lib/R/bin/Rscript --verbose Random_Analysis.R",shell=True).wait()
# Check if random analysis ran successfully
if Random_Analysis==0:
	print("Random Analysis ran successfully")
else: 
	print("Random Analysis did not ran successfully")

print("Producing example plots for fits of simulated data")
Simulated_fits=subprocess.Popen("/usr/lib/R/bin/Rscript --verbose Example_Plots.R", shell=True).wait()
if Simulated_fits==0:
	print("Simulated data example fit plots successfully produced")
else:
	print("Simulated data example fit plots not successfully produced")


print("Moving to real world data examples")

'''
print("Analysing real world Bd fungus data sets")
Bd_Analysis=os.system("python Fitting.py ../Data/Bd/Supercontig_1  10 22 ../Results/Bd_Results/Supercontig_1")
 Check if real data analysis ran successfully
if Bd_Analysis==0:
	print("Bd Analysis ran successfully")
else: 
	print("Bd Analysis did not ran successfully")
'''

######## Example of fitting script working on real world data. Analysis just on smallest supercontig and for just one sample to save time. All other supercontigs 
######## are not uploaded so running will produce warnings that the first 19 supercontigs are missing but will still work just compiling the single supercontig.
######## Results analysis and plots are done on the full fitting results as required for the report. For analysis to be run on this example results, required input would be: 
######## subprocess.Popen("/usr/lib/R/bin/Rscript --vanilla Plotting.R ../Results/Bd_Results/Supercontig_1.20 1",shell=True).wait()

print("Analysing example real world Bd fungus data sets")
Bd_Analysis_Example=os.system("python Fitting.py ../Data/Bd_Example/Supercontig_1  20 1 ../Results/Bd_Results/Supercontig_1.20")
#Check if real data analysis ran successfully
if Bd_Analysis_Example==0:
	print("Bd Analysis ran successfully")
else: 
	print("Bd Analysis did not ran successfully")

print("Generating plots of real world data fits")
Bd_Plots=subprocess.Popen("/usr/lib/R/bin/Rscript --vanilla Plotting.R ../Results/Bd_Results/Supercontig_1 22",shell=True).wait()
if Bd_Plots==0:
	print("Plots generated successfully")
else:
	print("Plots not generated successfully")


#print("Producing report")
#os.system("cd ../Writeup; ../Code/CompileLatex.sh MiniProject")
##Neaten up writeup directory by removing excess files
#os.system("cd ../Writeup; rm *.bbl *.blg *.xml *-blx.bib ")
#print("Project complete")
#print("Enjoy :)")

