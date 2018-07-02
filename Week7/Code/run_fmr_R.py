#! usr/bin/python3
""" Author - Oliver Tarrant
A python script to run the R script fmr.R
Returns the outputs from the script and an output if the script ran 
successfully or not
"""

import subprocess
#Run the subprocess
Task=subprocess.Popen("/usr/lib/R/bin/Rscript --verbose fmr.R",shell=True).wait()
# Check if subprocess ran successfully
if Task==0:
	print("Script ran successfully")
else: 
	print("Script did not ran successfully")
