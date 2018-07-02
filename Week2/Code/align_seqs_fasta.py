#! /usr/bin/python
""" Author - Oliver Tarrant
 Genetic sequence alignment script. Takes a csv file of two DNA sequences and aligns them 
returning the best alignment score"""

__author__ = 'Oliver Tarrant (oit16@ic.ac.uk)'
__version__ = '0.0.1'

import csv
import sys
# Checks that arguments given are correct else tells the user how to use the function
if len(sys.argv) < 3 : 
	with open('../Data/fasta/407228326.fasta' , 'rb') as seq:
		seq1 = list(csv.reader(seq, delimiter = '\n'))
		seq1 = seq1[1:]
		seq1 = sum(seq1,[])
		seq1 = ''.join(seq1)
	with open('../Data/fasta/407228412.fasta' , 'rb') as seqf:
		seq2 = list(csv.reader(seqf, delimiter = '\n'))
		seq2 = seq2[1:]
		seq2 = sum(seq2,[])
		seq2 = ''.join(seq2)			

	name1 = "too_few_args"
	name2 = "have_an_example" 
	
#Converts the fasta files into lists so that they can be aligned using the same method as in align_seq.py
else: 	
	seq1 = sys.argv[1] 
	seq2 = sys.argv[2]
	name1 = seq1.split("/",1000)[-1] #neatens up the file names for reference in output file good
	name2 = seq2.split("/",1000)[-1]
	with open(seq1, 'rb') as seq:
		seq1 = list(csv.reader(seq, delimiter = '\n'))
		seq1 = seq1[1:]
		seq1 = sum(seq1,[])
		seq1 = ''.join(seq1)
		 
	with open(seq2, 'rb') as seqf:
		seq2 = list(csv.reader(seqf, delimiter = '\n'))
		seq2 = seq2[1:]
		seq2 = sum(seq2,[])
		seq2 = ''.join(seq2)			

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
	#Open the output file and write the best alignment and alignment score in the file
	#f = open('../Results/align_%s_%s' % ('sys.argv[1]' , 'sys.argv[2]'),'w+') 
f = open('../Results/align_%s_%s' % (name1 , name2),'w+') 	
outtext = ["Best alignment:" + "\n", my_best_align + "\n", s1 + "\n", "\n","Best score:" + str(my_best_score)]
f.writelines(outtext) # requires a list input as generated above
f.close() 
