#! /usr/bin/python
"""Author - Oliver Tarrant
This is practical tuple.py. This takes the dataset birds and neatens it
up so that each species has it's own seperate line and the text has 
quotation marks removed and commas added between latin name, common name
and mass """

__author__ = 'Oliver Tarrant (oit16@ic.ac.uk)'
__version__ = '0.0.1'



birds = ( ('Passerculus sandwichensis','Savannah sparrow',18.7),
          ('Delichon urbica','House martin',19),
          ('Junco phaeonotus','Yellow-eyed junco',19.5),
          ('Junco hyemalis','Dark-eyed junco',19.6),
          ('Tachycineata bicolor','Tree swallow',20.2),
        )

# Birds is a tuple of tuples of length three: latin name, common name, mass.
# write a (short) script to print these on a separate line for each species
# Hints: use the "print" command! You can use list comprehensions!

# ANNOTATE WHAT EVERY BLOCK OR IF NECESSARY, LINE IS DOING! 

# ALSO, PLEASE INCLUDE A DOCSTRING AT THE BEGINNING OF THIS FILE THAT 
# SAYS WHAT THE SCRIPT DOES AND WHO THE AUTHOR IS
	
for latin_name, common_name, mass in birds: # defines each element of the tuples in birds
	print latin_name + ', ' + common_name + ', ' + str(mass) # prints a string with the elements combined and the text neatened

