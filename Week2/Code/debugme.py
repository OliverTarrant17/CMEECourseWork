#! usr/bin/python
""" Author - Oliver Tarrant
Script for practice debugging with using ipdb"""

def createabug(x):
	y = x**4
	z = 0.
	y = y/z
	return y
	
createabug(25)
