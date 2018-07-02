#! usr/bin/python
""" Author - Oliver Tarrant
 This file gives example code for reading a csv file and printing out the first column of each row
with the preceeding text "The species is". The second part of the code takes the file testcsv.csv 
and then returns just the first and last columns (species and body mass) and saves the file as 
body mass.csv (saved in sandbox)"""

import csv

# Read a file containing:
# 'Species','Infraorder','Family','Distribution','Body mass male (Kg)'
f = open('../Data/testcsv.csv','rb')

csvread = csv.reader(f)
temp = [] # Create a blank array
for row in csvread:
	temp.append(tuple(row)) # for each row adds the data from the csv to the array in the form of a tuple
	print row  # prints out the entire information about the species
	print "The species is", row[0] #picks out the species name
	
f.close()

# write a file containing only species name and Body mass
f = open('../Data/testcsv.csv','rb') # opens the csv to read
g = open('../Sandbox/bodymass.csv','wb') # creates a csv to write

csvread = csv.reader(f) # assign names to the open csv
csvwrite = csv.writer(g) 
for row in csvread:
	print row # print rows in the csv to be read
	csvwrite.writerow([row[0], row[4]]) #writes in the new csv the species name and body mass
	
f.close()
g.close() #close the files
