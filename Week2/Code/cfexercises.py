#! /usr/bin/python

"""Author - Oliver Tarrant 
Some exercises derived from original script of cfexercises to convert 
it into a module"""
__author__ = 'Oliver Tarrant (oit16@ic.ac.uk)'
__version__ = '0.0.1'

import sys # module to interface our program with operating system

# How many times will 'hello' be printed?
# 1)

for i in range(3,17):
	# prints hello for each value in the index within the range 3,17
	print 'hello'
	# answer = 14

# 2) 

for j in range(12):
	#Prints hello each time j modulo 3 = 0 i.e for 0,3,6,9
	if j % 3 == 0:
		print 'hello'
	# answer = 4

# 3)

for j in range(15):
	#Prints hello each time j  modulo 5 is 3 or j modulo 4 is 3
	if j % 5 == 3:
		print 'hello'
	elif j % 4 == 3:
		print 'hello'
	# answer = 5
	
# 4) 

z = 0
while z != 15:
	# Prints hello whenever z is not equal to 15. z starts at 0 and increases by 3 each 
	# pass through the while loop
	print 'hello'
	z = z + 3
	# answer = 5
	
# 5) 

z = 12	
while z < 100:
	# z starts at 12 and increases by 1 each run through the loop
	#until it reaches 18 then enters the elif section and prints hello. 
	#continues to increase to 31 which then enters the if statement and
	#prints hello 7 times as k counts from 0 to 6 (range(7))
	if z == 31:
		for k in range(7):
			print 'hello'
	elif z == 18:
		print 'hello'
	z = z + 1
	# answer = 8 
	
# What does fooXX do?

def foo1(x):
	"""Returns the square root of x"""
	return x ** 0.5


def foo2(x,y):
	"""Returns the larger of x and y"""
	if x > y:
		return x
	return y
	
	

def foo3(x,y,z):
	"""Reorders x and y to put largest first then does the same with the new value in the 
	y position and the z"""
	if x > y:
		tmp = y 
		y = x
		x = tmp
	if y > z:
		tmp = z
		z = y
		y = tmp
	return [x,y,z]
	
	
	
def foo4(x):
	"""Returns x factorial"""
	result = 1
	for i in range(1, x + 1):
		result = result * i
	return result
	


# This is a recursive function, meaning that the function calls itself
# read about it at 
# en.wikipedia.org/wiki/Recursion_(computer_science)
"""Returns x factorial"""
def foo5(x):
	if x == 1:
		return 1
	return x * foo5(x - 1)
	
foo5(10)	


def main(argv):
# prints examples of each fooxx function running
	print foo1(25)
	print foo2(33,22)
	print foo3(120,235,12)
	print foo4(8)
	print foo5(3)
	return 0		

if (__name__ == "__main__"):
	status = main(sys.argv)
	sys.exit(status)

