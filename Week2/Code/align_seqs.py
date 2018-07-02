#! /usr/bin/python
""" AUthor - Oliver Tarrant
 Genetic sequence alignment script. Takes a csv file of two DNA sequences and aligns them 
returning the best alignment score"""

__author__ = 'Oliver Tarrant (oit16@ic.ac.uk)'
__version__ = '0.0.1'

import csv
import sys

# Opening the input csv file and reads the two sequences as a list, 
#donoting each sequence as seq1 & seq 2 respectively 
with open('../Data/Sequences.csv', 'rb') as seqcsv:
	seq = list(csv.reader(seqcsv, delimiter = ','))
	seq1 = seq[0][0]
	seq2 = seq[0][1]
# These are the two sequences to match
seqcsv.close()
	# assign the longest sequence s1, and the shortest to s2
# l1 is the length of the longest, l2 that of the shortest
l1 = len(seq1)
l2 = len(seq2)
if l1 >= l2:
	s1 = seq1
	s2 = seq2
else:
	s1 = seq2
	s2 = seq1
	l1, l2 = l2, l1 # swap the two lengths

# function that computes a score
# by returning the number of matches 
# starting from arbitrary startpoint
def calculate_score(s1, s2, l1, l2, startpoint):
	"""Given two strings with their lengths given and a start point
	this function aligns the two sequences starting at this start point
	and returns the resulting alignment along with its score"""
	# startpoint is the point at which we want to start
	matched = "" # contains string for alignement
	score = 0
	for i in range(l2):
		if (i + startpoint) < l1:
			# if its matching the character
			if s1[i + startpoint] == s2[i]:
				matched = matched + "*"
				score = score + 1
			else:
				matched = matched + "-"
	return score
	# now try to find the best match (highest score)
my_best_align = None
my_best_score = -1
for i in range(l1):
	z = calculate_score(s1, s2, l1, l2, i)
	if z > my_best_score:
		my_best_align = "." * i + s2
		my_best_score = z
	#creates a new output file to write results in
f = open('../Results/Sequences_aligned.txt','w+')
outtext = ["Best alignment:" + "\n", my_best_align + "\n", s1 + "\n", "\n","Best score:" + str(my_best_score)]
f.writelines(outtext) # requires a list input as generated above
f.close() 
