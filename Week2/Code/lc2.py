#! /usr/bin/python
"""Author - Oliver Tarrant
This is practical lc2. With the rainfall data from the met office for 1910 
This script first creates a list using list comprehension of the months with 
rainfall over 100mm with the corresponding rainfall for each month.
Then the script creates a new list using list comprehension of month with 
rainfall under 50mm, again with corresponding rainfall. 
Finally it recreates these two lists again but this time using 
loops rather than list comprehension."""

######## Instructions #########
# (1) Use a list comprehension to create a list of month,rainfall tuples where
# the amount of rain was greater than 100 mm.
 
# (2) Use a list comprehension to create a list of just month names where the
# amount of rain was less than 50 mm. 

# (3) Now do (1) and (2) using conventional loops (you can choose to do 
# this before 1 and 2 !). 

# ANNOTATE WHAT EVERY BLOCK OR IF NECESSARY, LINE IS DOING! 

# ALSO, PLEASE INCLUDE A DOCSTRING AT THE BEGINNING OF THIS FILE THAT 
# SAYS WHAT THE SCRIPT DOES AND WHO THE AUTHOR IS
# Average UK Rainfall (mm) for 1910 by month
# http://www.metoffice.gov.uk/climate/uk/datasets
#################################

__author__ = 'Oliver Tarrant (oit16@ic.ac.uk)'
__version__ = '0.0.1'

rainfall = (('JAN',111.4),
            ('FEB',126.1),
            ('MAR', 49.9),
            ('APR', 95.3),
            ('MAY', 71.8),
            ('JUN', 70.2),
            ('JUL', 97.1),
            ('AUG',140.2),
            ('SEP', 27.0),
            ('OCT', 89.4),
            ('NOV',128.4),
            ('DEC',142.2),
           )  # enters in the rainfall data

###############Creates a list of months and corresponding rainfall for month where the
#rainfall is >100mm. The second list is of the months whose rainfall is <50mm
#These lists are created with list comprehension#############

#1.

over_100 = set([month[0:2] for month in rainfall if month[1] > 100.0]) # creates a set of the indexs of 0:2 (2 not included) for the months in rainfall where the index 1 is greater than 100mm
print over_100 # prints the corresonding list

#2.

under_50 = set([month[0] for month in rainfall if month[1] < 50.0]) # creates a set of the names (index 1) for the months in rainfall where the index 1 is less than 50mm
print under_50 # prints the corresonding list


##########Creates a list of months and corresponding rainfall for month where the
#rainfall is >100mm. The second list is of the months whose rainfall is <50mm
#These lists are created with loops###############

#3.

over_100_loop = set() #creates an empty set 
for month in rainfall: # creates a for loop to inspect the elements of rainfall
	if month[1] > 100: # checks which months are over 100mm
		over_100_loop.add(month[0:2]) # adds those months with rainfall over 100mm and their rainfall to the set
print over_100_loop # prints the set when all months are checked

under_50_loop = set() #creates an empty set
for month in rainfall: # creates a loop to inspect the elements of rainfall
	if month[1] < 50: #checks which months have rainfall under 50mm
		under_50_loop.add(month[0]) #adds those months whose rainfall is under 50mm
print under_50_loop # prinst the set when all months are checked


