#! /usr/bin/python
"""Author - Oliver Tarrant
This is practical dictionary.py. This script creates a dictionary called 
taxa_dic which is printed out as a result. This dictionary is formed from 
analysing the dataset taxa and creating a set of taxa for each of the order 
names that are there."""

__author__ = 'Oliver Tarrant (oit16@ic.ac.uk)'
__version__ = '0.0.1'

################INSTRUCTIONS##################
# Write a short python script to populate a dictionary called taxa_dic 
# derived from  taxa so that it maps order names to sets of taxa. 
# E.g. 'Chiroptera' : set(['Myotis lucifugus']) etc. 

# ANNOTATE WHAT EVERY BLOCK OR IF NECESSARY, LINE IS DOING! 

# ALSO, PLEASE INCLUDE A DOCSTRING AT THE BEGINNING OF THIS FILE THAT 
# SAYS WHAT THE SCRIPT DOES AND WHO THE AUTHOR IS

# Write your script here:
##############################################
taxa = [ ('Myotis lucifugus','Chiroptera'),
         ('Gerbillus henleyi','Rodentia',),
         ('Peromyscus crinitus', 'Rodentia'),
         ('Mus domesticus', 'Rodentia'),
         ('Cleithrionomys rutilus', 'Rodentia'),
         ('Microgale dobsoni', 'Afrosoricida'),
         ('Microgale talazaci', 'Afrosoricida'),
         ('Lyacon pictus', 'Carnivora'),
         ('Arctocephalus gazella', 'Carnivora'),
         ('Canis lupus', 'Carnivora'),
        ] #enters the taxa database
        
orders = set([organism[1] for organism in taxa]) # creates a set of all the different orders in the taxa database
dic = {} # creates an empty dictionary
for x in orders: # creates a for loop for each element of set orders
	taxafound_x = list([organism[0] for organism in taxa if organism[1] == '%s' % x]) # for each order this checks the database and creates a list of those organisms for that order 
	new_entry = {'%s' % x: taxafound_x}  # Creates a new entry ready for the dictionary with the order for the current for loop as the key and corresponding list of organisms built line above
	dic.update(new_entry) # adds this new entry to the dictionary
print dic # prints the resulting dictionary







