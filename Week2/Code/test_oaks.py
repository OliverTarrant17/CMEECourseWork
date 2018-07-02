#! /usr/bin/python
"""Author - Oliver Tarrant
Script set up to read a data file of different species and return a list of just those that are oaks"""
import csv
import sys
import ipdb
import doctest
ipdb.set_trace()
#Define function
def is_an_oak(name):
    """ Returns True if name is starts with 'quercus '
        >>> is_an_oak('quercus ')
        True
        >>> is_an_oak('Quercus ')
        True
        >>> is_an_oak('Fagus sylvatica')
        False
        >>> is_an_oak('Quercuss')
        False
        >>> is_an_oak('squercus ')
        False
        >>> is_an_oak('Quercus') #note no space as biuilt into function to avoid longer words
        False
        >>> is_an_oak('blah Quercus ')
        False
    """
    na = name.lower()
    x = na.startswith('quercus ')  
    return x
    
print(is_an_oak.__doc__)

def main(argv): 
    f = open('../Data/TestOaksData.csv','rb')
    g = open('../Results/JustOaksData.csv','wb')
    taxa = csv.reader(f)
    csvwrite = csv.writer(g)
    oaks = set()

    for row in taxa:
        print row
        print "The genus is", row[0]
        if is_an_oak(row[0]+" "): # added space after row[0] to pick up unwanted trailing letters
            print row[0]
            print 'FOUND AN OAK!'
            print " "
            csvwrite.writerow([row[0], row[1]])    
    
    return 0
    
if (__name__ == "__main__"):
    status = main(sys.argv)

doctest.testmod()
