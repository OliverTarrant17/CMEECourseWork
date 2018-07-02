#! usr/bin/python3

""" Author : Oliver Tarrant
A script giving an example of the uses of different regular exprressions
"""

import re

my_string = "a given string"

# find a space in the string
match = re.search(r'\s', my_string)

print(match)
# this should print something like
# <_sre.SRE_Match object at 0x93ecdd30>

# now we can see what has matched
match.group()

match = re.search(r's\w*', my_string)

# this should return "string"
match.group()

# NOW AN EXAMPLE OF NO MATCH:
# find a digit in the string
match = re.search(r'\d', my_string)

# this should print "None"
print(match)

# Further example

my_string = 'an example'
match = re.search(r'\w*\s', my_string)

if match:
	print('found a match', match.group())
else:
	print('did not find a match')

# some more examples 

# some basic examples
match = re.search(r'\d', "it takes 2 to tango")
print(match.group()) #print 2

match = re.search(r'\s\w*\s', 'once upon a time')
match.group() # ' upon '

match = re.search(r'\s\w{1,3}\s', 'once upon a time')  # match space, alphanumeric (atleast 1 but not more than 3 times) then space
match.group() # ' a '

match = re.search(r'\s\w*$', 'once upon a time') # match space, alphanumeric  (n=0 to any times), end of line
match.group() # ' time'

match = re.search('\w*\s\d.*\d', 'take 2 grams of H20') 
# match 0+ alphanumeric then space then numeric then 0+ any character then numeric
match.group() # 'take 2 grams of H2'

match = re.search(r'^\w*.*\s', 'once upon a time') # match beginign of line, 0+ alphanumeric, 0+ any, space
match.group() # 'once upon a '
## Note that *, =, and {} are all "greedy":
## They repeat the previous regex token as many times as possible
## As a result, they may match more text than you want

## To make non-greedy, use ?:
match = re.search(r'^\w*.*?\s', 'once upon a time')
match.group() # 'once '

## To further illustrate greediness, let's try match an HTML tag:
match = re.search(r'<.+>', 'This is a <EM>first</EM> test') #match <, any charater 1+ times, >
match.group() # '<EM>first</EM>'
## But we didn't want this: we wanted just <EM>
## It's because + is greedy!

## Instead we can make + "lazy"!
match = re.search(r'<.+?>', 'This is a <EM>first</EM> test')
match.group() # '<EM>'

## Ok, moving on from the greed and laziness
match = re.search(r'\d*\.?\d*','1432.75+60.22i') # note "\" before "."
# match 0+numeric, \.? matches a "." once, then 0+ numerics
match.group() # '1432.75'

match = re.search(r'\d*\.?\d*','1432+60.22i')
match.group() # '1432'

match = re.search(r'[AGTC]+', 'the sequence ATTCGT') # match any charcters listed (A,T,C,G)
match.group() # 'ATTCGT'

re.search(r'\s+[A-Z]{1}\w+\s\w+', 'The bird-shit frog''s name is Theloderna asper').group()
# match 1+ spaces, any capital letter once, 1+ alphanumeric, space, 1+ alphanumeric 
# ' Theloderma asper'
## NOTE THAT I DIRECTLY RETURNED THE RESULT BY APPENDING .gorup()
