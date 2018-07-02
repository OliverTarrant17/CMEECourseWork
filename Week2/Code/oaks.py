#! usr/bin/python
""" Author - Oliver Tarrant
A script to return which species are oaks from a list of taxa"""


## Let's find just those taxa that are oak trees from a list of species

taxa = [ 'Quercus robur', 'Fraxinus excelsior', 'Pinus sylvestris', 'Quercus cerris', 'Quercus petraea' ]
# initial list of species
def is_an_oak(name): # creates a function to test if a species is an oak or not
	"""Checks the argument and returns true is it is an oak"""
	return name.lower().startswith('quercus ') #returns a True or False depending if it is an oak
	
## call using for loops
oaks_loops = set()
for species in taxa:
	if is_an_oak(species):
		oaks_loops.add(species)
print oaks_loops # checks using above function if each is an oak and returns the set of oaks

## call using list comprehensions
oaks_lc = set([species for species in taxa if is_an_oak(species)])
print oaks_lc  # checks each iteam in the list if it is an oak or not and creates a set of those that are

## call and get names in UPPER CASE using for loops
oaks_loops = set()
for species in taxa:   #checks each iteam in the list
	if is_an_oak(species): # checks using first function if it is an oak
		oaks_loops.add(species.upper()) # adds thos that are oaks in upper case to the set oaks_loops
print oaks_loops # prints the set of oaks

## call and get names in UPPER CASE usign list comprehension
oaks_lc = set([species.upper() for species in taxa if is_an_oak(species)]) #defines the set and tells you to add in upper case all those species in taxa that return True to is_an_oak
print oaks_lc #prints the set 
