#! usr/bin/python3
""" Author - Oliver Tarrant
A script to practice subprocessing by running an R script through
python
"""
import subprocess

subprocess.Popen("/usr/lib/R/bin/Rscript --verbose TestR.R > \
../Results/TestR.Rout 2> ../Results/TestR_errFile.Rout",\
 shell=True).wait()
 
# Run through R studio and save results to TestR.Rout, if errors then 
# send results to the error file TestR_errFile.Rout
# The verbose command ensures all the output is printed
