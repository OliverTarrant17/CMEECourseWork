#! /usr/bin/python

""" Author - Oliver Tarrant
 Description of this program
	You can use several lines
	docstring can be accesed at run time"""
	
__author__ = 'Oliver Tarrant (oit16@ic.ac.uk)'
__version__ = '0.0.1'

# imports
import sys # module to interface our program with the operating system

# constants can go here


# functions can go here
def main(argv):
		print('This is a boilerplate') # NOTE: indented using 2 tabs
		return 0
		
if (__name__== "__main__"): # makes sure thr "main" function is called from command line
		status = main(sys.argv)
		sys.exit(status)
