#! usr/bin/python
"""Author - Oliver Tarrant
This file gives the example code for opening a file for reading using python.
Then the code writes a new file called testout.txt which is the output of 1-100 
and saves this file in Sandbox folder (see below). Finally the code gives an example of 
storing objects for later use. In this example my_dictionary is stored as the file testp.p
in sandbox. Pickle is used to serialize the objects hieracy"""


########################
# FILE INPUT
########################
# Open a file for reading
f = open('../Sandbox/test.txt',	'r')
# use "implicit" for loop:
# if the object is a file, python will cycle over lines
for line in f:
	print line, # the "," prevents adding a new line
		
# close the file
f.close()

# same example, skip blank lines
f = open('../Sandbox/test.txt',	'r')
for line in f:
	if len(line.strip()) > 0: #removes trailing and leading spaces from line and determines if it is non blank
		print line,
		
f.close()


#################
# FILE OUTPUT
#################
list_to_save = range(100)

f = open('../Sandbox/testout.txt','w')
for i in list_to_save:
	f.write(str(i) + '\n') ## Add a new line at the end
	
f.close()

####################
# STORING OBJECTS
####################
# To save an object (even complex) for later use
my_dictionary = {"a key": 10, "another key": 11}

import pickle

f = open('../Sandbox/testp.p','wb') ## note the b: accept binary files
pickle.dump(my_dictionary, f)
f.close()
## Load the data again
f = open('../Sandbox/testp.p','rb')
another_dictionary = pickle.load(f)
f.close()

print another_dictionary
