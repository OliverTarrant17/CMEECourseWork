#! /usr/bin/python

""" Author - Oliver Tarrant 
Some functions exemplfying the use of control statements"""

__author__ = 'Oliver Tarrant (oit16@ic.ac.uk)'
__version__ = '0.0.1'

# imports
import sys 
import doctest # Import the doctest module


def even_or_odd(x=0): #if not specified, x should take the value 0
	"""Find whether a number x is even or odd.
	
	>>> even_or_odd(10)
	'10 is Even!'
	
	>>> even_or_odd(5)
	'5 is Odd!'
	
	whenever a float if provided, then the closest integer is used:
	>>> even_or_odd(3.2)
	'3 is Odd!'
	
	In the case of negative numbers, the positive is taken:
	>>> even_or_odd(-2)
	'-2 is Even!'
	
	"""
	# define function to be tested
	
	if x % 2 == 0: #The conditional if. Checking if x divided by 2 leaves remainder 0
		return "%d is Even!" % x   # %d is a space holder for a number %x afterwards is needed to refer to x beingn where the number is taken from
	return "%d is Odd!" % x

###### Suppressed this block as just using docstring tests to detrmine if the function works so don't want to run unnessary code #########
	

#~ def main(argv):
	#~ print even_or_odd(22)
	#~ print even_or_odd(33)
	#~ return 0


	
#~ if (__name__ == "__main__"):
	#~ status = main(sys.argv)
	#~ sys.exit(status)
	
	
##########################################	

doctest.testmod() # To run with embedded tests


