#! usr/bin/python

""" Author - Oliver Tarrant 
A python version of Vectorize1.R which uses vectorisation 
to summ all the elements of a 1000x1000 matrix of random uniform
variables"""
import scipy as sc
import timeit
import time


M = sc.random.uniform(0,1,[1000,1000]) # Creates a matrix of random
									   # unifrom variables

def sum_all_elements(x): # define a function
	"""A function that sums all the elements of an array entered to it"""
	Dimensions = sc.shape(x) # Saves the dimensions of the array
	Tot = 0 # Sets an initial total to 0
	for i in range(Dimensions[0]): # cycles through the rows
		for j in range(Dimensions[1]): # cycles through the columns
			Tot = Tot + x[i,j] # Adds each element one by one
	return Tot # Returns the sum
	

start = time.time() # takes a start time
sum_all_elements(M) # runs the function
print "sum_all_elements(M) (non vectorized version) takes %f s to run." % (time.time() - start)
# read out message with inputed value taken the current time - start time
start = time.time()
sc.sum(M)
print "sc.sum(M) (vectorized version) takes %f s to run." % (time.time() - start)
