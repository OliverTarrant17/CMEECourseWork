#! /usr/bin/python
"""Author - Oliver Tarrant
lc1 practical in which the list of birds is taken and list comprehension is used to create
three seperate lists, first with the latin names, second with common names and third with 
mean body mass. Then three further lists are created. These are repeats of the first three 
but are formed using loops rather than list comprehension"""

################INSTRUCTIONS###################
#(1) Write three separate list comprehensions that create three different
# lists containing the latin names, common names and mean body masses for
# each species in birds, respectively. 

# (2) Now do the same using conventional loops (you can shoose to do this 
# before 1 !). 

# ANNOTATE WHAT EVERY BLOCK OR, IF NECESSARY, LINE IS DOING! 

# ALSO, PLEASE INCLUDE A DOCSTRING AT THE BEGINNING OF THIS FILE THAT 
# SAYS WHAT THE SCRIPT DOES AND WHO THE AUTHOR IS
################################################

__author__ = 'Oliver Tarrant (oit16@ic.ac.uk)'
__version__ = '0.0.1'

import sys # module to interface our program with the operating system


birds = ( ('Passerculus sandwichensis','Savannah sparrow',18.7),
          ('Delichon urbica','House martin',19),
          ('Junco phaeonotus','Yellow-eyed junco',19.5),
          ('Junco hyemalis','Dark-eyed junco',19.6),
          ('Tachycineata bicolor','Tree swallow',20.2),
         )   # enters the dataset birds
         
###############Creating lists of latin names, common names and body masses respectively using list comprehension###########
 
 #1.     
    
Latin_names = set([bird[0] for bird in birds]) # creates a set of all the zero index enties (latin names) from all entries in dataset birds
print Latin_names # prints the resulting list of latin names

Common_names = set([bird[1] for bird in birds]) # creates a set of all the 1 index entries (common names) from all entries in dataset birds
print Common_names # prints the resulting list of common names

Body_masses = set([bird[2] for bird in birds]) # creates a set of all the last (2) index entries (body masses) from all entries in dataset birds
print Body_masses # prints the resulting list of body masses


###############Creating lists of latin names, common names and body masses respectively using loops################

#2.

latin_names_loops = set() # defines an empty set for latin names
for bird in birds: # sets up a for loop to check all elements of birds
	latin_names_loops.add(bird[0]) # adds the zero index of each entry in birds to the set created
print latin_names_loops # prints the resulting list

common_names_loops = set() # defines an empty set for common names
for bird in birds: # sets up a for loop to check all elements of birds
	common_names_loops.add(bird[1]) # adds the 1 index of each entry in birds to the set created
print common_names_loops # prints the resulting list

body_masses_loops = set() # defines an empty set for bady masses
for bird in birds: # sets up a for loop to check all elements of birds
	body_masses_loops.add(bird[2]) # adds the last (2) index of each entry in birds to the set created
print body_masses_loops # prints the resulting list

