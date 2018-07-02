#! usr/bin/python3
""" Author - Oliver Tarrant
	A script that searches through a text file of animal taxa and returns
	the Kingdom, phylum and species for each organism
"""
import re

# Read the file
f = open('../Data/blackbirds.txt', 'r')
text = f.read()
f.close()

# remove \t\n and put a space in:
text = text.replace('\t',' ')
text = text.replace('\n',' ')

# note that there are "strange characters" (these are accents and
# non-ascii symbols) because we don't care for them, first transform
# to ASCII:
text = text.encode('ascii', 'ignore').decode()

# Now extend this script so that it captures the Kingdom, 
# Phylum and Species name for each species and prints it out to screen neatly.

Kingdoms = re.findall(r'Kingdom\s[\w]*\s',text) # Creates a list of the kingdoms


Phylums = re.findall(r'Phylum\s[\w]*\s',text) # Creates a list of the Phylums	

# strip trailing spaces
for i in range(len((Kingdoms))):
	Kingdoms[i]=Kingdoms[i].strip(" ")
	Phylums[i]=Phylums[i].strip(" ")

Species = re.findall(r'Species\s[^\)]*\)',text) # Creates a list of Species

l = list(zip(Kingdoms,Phylums,Species)) # Converts the lists to tuples

# Print all results each on a new line
for i in range(len(l)):
	print(l[i])
