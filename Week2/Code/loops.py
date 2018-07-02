#! usr/bin/python
""" Author - Oliver Tarrant
 A script demonstrating the differnt ways of using loops in python"""

# for loops in Python
for i in range(5):
	print i # prints numbers 0,1,2,3,4 (note starts at 0 as python index starts at 0)
	

my_list = [0,2,"geronimo!", 3.0, True, False]
for k in my_list:
	print k
	# returns my_list, each entry on a new line
	
total = 0
summands = [0, 1, 11, 111, 1111]
for s in summands:
	total = total + s
	print total + s   # prints the cumulative sum of list summands
	

# while loops in Python
z = 0
while z < 100: # checks if value of z is < 100 and if so enters the while loop
	z = z + 1 # increases z to next integer
	print (z) # prints this integer then returns to begining of while loop
			  # ie checks if this value is still less than 100
			  
b = True
while b:
	print "GERONIMO! infinite loop! ctrl+c to stop!"
	# ctrl + c to stop
	
