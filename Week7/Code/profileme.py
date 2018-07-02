#! usr/bin/python
"""Author - Oliver Tarrant
A script to practice profiling on"""
def a_useless_function(x):
	"""counts from 0 to 100000000"""
	y = 0
	# eight zeros!
	for i in xrange(100000000):
		y = y + i
	return 0
	
def a_less_useless_function(x):
	"""Counts from 0 to 100000"""
	y = 0
	# five zeros!
	for i in xrange(100000):
		y = y + i
	return 0
	
def some_function(x):
	"""Perfoms a_useless_function and a_less_useless_function"""
	print x
	a_useless_function(x)
	a_less_useless_function(x)
	return 0
	
	
some_function(1000)
