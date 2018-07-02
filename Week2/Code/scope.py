#! usr/bin/python
""" Author - Oliver Tarrant
Demonstrates the use of global variables. The first funtion failes to run
		properly because the variable _a_global is not defined as a global variable
		whilst the second one does as it is correctly defined"""

## Try this first

#~ _a_gloabl = 10

#~ def a_function():
	#~ _a_global = 5
	#~ _a_local = 4
	#~ print "Inside the function, the value is ", _a_global
	#~ print "Inside the function, the value is ", _a_local
	#~ return None
	
#~ a_function()
#~ print "Outside the function, the value is ", _a_global



## Now try this

_a_global = 10

def a_function():
	global _a_global # defined as a global variable
	_a_global = 5
	_a_local = 4
	print "Inside the function the value is ", _a_global
	print "Inside the function the value is ", _a_local
	return None
	
a_function()
print "Outside the function, the value is", _a_global
