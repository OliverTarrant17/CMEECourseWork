#! /usr/bin/python

""" Author - Oliver Tarrant
 Some functions exemplfying the use of control statements"""
#docstrings are considered part of the running code (normal comments are
#stripped) . Hence you can access your docstrings at run time.
__author__ = 'Oliver Tarrant (oit16@ic.ac.uk)'
__version__ = '0.0.1'

# imports
import sys # module to interface our program with the operating system

# constants can go here
def even_or_odd(x=0): #if not specified, x should take the value 0
	
	"""Find whether a number x is even or odd."""
	if x % 2 == 0: #The conditional if. Checking if x divided by 2 leaves remainder 0
		return "%d is Even!" % x   # %d is a space holder for a number %x afterwards is needed to refer to x beingn where the number is taken from
	return "%d is Odd!" % x
	
def largest_divisor_five (x=120) :
	"""Find which is the largest divisor of x amoung 2,3,4,5."""
	largest = 0
	if x % 5 == 0:
		largest = 5
	elif x % 4 == 0: #means "else if" 
		largest = 4
	elif x % 3 == 0:
		largest = 3
	elif x % 2 == 0:
		largest = 2
	else: #when all other (if, elif) conditions are not met
		return "No divisor found for %d!" % x # Each function can return a variable
	return "The largest divisor of %d is %d" % (x, largest) # Note tuple needed for multiple stored values

def is_prime(x=70):
	"""Find whether an integer is prime."""
	for i in range (2,x): # "range" returns a sequence of integers
		if x % i == 0:
			print "%d is not a prime: %d is a divisor" % (x,i) #Print formatted text "%d %s %f %e" % (20,"30",0.0003,0.00003)
			
			return False
	print "%d is a prime!" % x
	return True
	
def find_all_primes(x=22):
	"""Find all the primes up to x"""
	allprimes=[]    # sets initial list to 0
	for i in range(2, x + 1): # gives range to check in
		if is_prime(i): # uses above function to test if each number in range is prime
			allprimes.append(i) # if a number in the range is prime then it is added to the list of primes
	print "There are %d primes between 2 and %d" % (len(allprimes), x)  # returns the length of the list of primes
	return allprimes #returns the primes
	
def main(argv):
	# sys.exit("don't want to do this right now!")
	print even_or_odd(22)
	print even_or_odd(33)
	print largest_divisor_five(120)
	print largest_divisor_five(121)
	print is_prime(60)
	print is_prime(59)
	print find_all_primes(100) # demonstrates that functions work
	return 0   # sign of success
	
if (__name__ == "__main__"):
	status = main(sys.argv)
	sys.exit(status)
