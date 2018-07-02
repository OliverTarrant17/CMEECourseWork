#! usr/bin/python

""" Author - Oliver Tarrant
A python script which takes a csv file of data about trees as an
argument and returns a new csv file with the same data and an extra column
of their height. This is calculated using the triginometic relationship
between distance and angle to the trees top""" 

import sys
import csv
import scipy as sc
#import ipdb 
#ipdb.set_trace()

if len(sys.argv) < 2:
	print "Please run script with a csv file in the command line" 
else:	
	
	data = sys.argv[1] # takes data file from command line
	name = data.split("/",10000)[-1] # removes path from file name
	name = name.split(".csv",1)[0] # removes .csv
	with open(data,'rb') as tree_data: #opens data file
		with open('../Results/%s_heights.csv' % name,'wb') as tree_out:
			#opens a output file with name of input file included in name
			out = csv.writer(tree_out) #names files for easy calling
									   #and manipulating
			data = csv.reader(tree_data)
			
			A = [] # Creates a blank array
			row = next(data) #goes to first row
			row.append('Height') # Adds a new header
			A.append(row)  # adds the headers to A
			
			for row in data: #cycles through the data
				R = float(row[2])*(sc.pi/180) #calculates radians for each tree
				H = float(row[1])*sc.tan(R) # height for each tree
				print "The tree height is: " , H  # prints the tree height
				row.append(H) # adds height value to each row
				A.append(row) #adds row including height to A
				
			out.writerows(A) # writes all of A to output file
	
		
	 
