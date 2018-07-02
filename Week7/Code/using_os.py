#! usr/bin/python3
""" Author - Oliver Tarrant
This is a script using subprocesses to crawl through my home directory
and then returns a list of the files whose name begins with C
"""

# Use the subprocess.os module to get a list of files and  directories 
# in your ubuntu home directory 

# Hint: look in subprocess.os and/or subprocess.os.path and/or 
# subprocess.os.walk for helpful functions

import subprocess

#################################
#~Get a list of files and 
#~directories in your home/ that start with an uppercase 'C'

# Type your code here:

# Get the user's home directory.
home = subprocess.os.path.expanduser("~")

# Create a list to store the results.
FilesDirsStartingWithC = []

# Use a for loop to walk through the home directory.

for (dir, subdir, files) in subprocess.os.walk(home):
	for name in dir:
		if name[0].startswith("C"):
			FilesDirsStartingWithC.append(name)
	for name in subdir:
		if name[0].startswith("C"):
			FilesDirsStartingWithC.append(name)	
	for name in files:	
		if name[0].startswith("C"):
			FilesDirsStartingWithC.append(name)
  
#################################
# Get files and directories in your home/ that start with either an 
# upper or lower case 'C'

# Type your code here:
FilesDirsStartingWithC_c=FilesDirsStartingWithC
for (dir, subdir, files) in subprocess.os.walk(home):
	for name in dir:
		if name[0].startswith("c"):
			FilesDirsStartingWithC_c.append(name)
	for name in subdir:
		if name[0].startswith("c"):
			FilesDirsStartingWithC.append(name)
	for name in files:	
		if name[0].startswith("c"):
			FilesDirsStartingWithC_c.append(name)
#################################
# Get only directories in your home/ that start with either an upper or 
#~lower case 'C' 

# Type your code here:

DirsStartingWithC_c=[]
for (dir, subdir, files) in subprocess.os.walk(home):
	for name in dir:
		if name[0].startswith("C"):
			DirsStartingWithC_c.append(name)
	for name in dir:	
		if name[0].startswith("c"):
			DirsStartingWithC_c.append(name)
	for name in subdir:
		if name[0].startswith("C"):
			DirsStartingWithC_c.append(name)
	for name in subdir:
		if name[0].startswith("c"):
			DirsStartingWithC_c.append(name)

print('The files and directories begining with "C" are:')
print(set(FilesDirsStartingWithC))
print('The files and directories starting with "C" or "c" are:')
print(set(FilesDirsStartingWithC_c))
print('The directories starting with "C" or "c" are:')
print(set(DirsStartingWithC_c))
