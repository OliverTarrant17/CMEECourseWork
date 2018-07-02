#! usr/bin/python

""" Author - Oliver Tarrant
A python version of Vectorize2.R. A vectorized version of the 
stochastic Ricker model"""

import scipy as sc
import time
import timeit


def stochrick(p0=sc.random.uniform(0.5,1.5,1000),r=1.2,k=1,sigma=0.2,numyears=100):
	N = sc.empty(shape=(numyears, len(p0)))
	N[0,]=p0
	for pop in range(len(p0)):
		for yr in range(1,numyears):
			N[yr,pop] = N[yr-1,pop]*sc.exp(r*(1-N[yr-1,pop]/k)+sc.random.normal(0,sigma,1))  #(mean,sd,n)
			
	return N 
start = time.time()
stochrick()
print "stockrick takes %f s to run!" %(time.time()-start)

def stochrickvect(p0=sc.random.uniform(0.5,1.5,1000),r=1.2,k=1,sigma=0.2,numyears=100):
	N = sc.empty(shape=(numyears,len(p0)))
	N[0,]=p0
	for yr in range(1,numyears):
		N[yr,] = N[yr-1,]*sc.exp(r*(1-N[yr-1,]/k)+sc.random.normal(0,sigma,1))
		
	return N
start = time.time()	
stochrickvect()
print "stochrickvect takes %f s to run!" %(time.time()-start)	




