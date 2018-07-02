#! usr/bin/python3

import sys
import gzip
import math
import numpy as np

input = sys.argv[1]
output = sys.argv[2]
NSAMS = int(sys.argv[3])
ploidies=8 # make input argument?
Overall_p=np.zeros(ploidies,float) # probabilities
Sample_p=np.zeros((NSAMS,ploidies),float) # NSAMSxploidies array for probabilities of each ploidy for each sample
with gzip.open(input,'rt') as file:
    for line in file:
        Data=line.strip('\n').split('\t') # sepereate by tabs and strip new line character
        
        j=0
        for(i in range(ploidies)):
            p[0]=p[0]+math.exp(Data[7])+math.exp(Data[8])
            p[1]=p[1]+math.exp(Data[9])+math.exp(Data[10])+math.exp(Data[11])
            p[2]=p[2]+math.exp(Data[12])+math.exp(Data[13])+math.exp(Data[14])+math.exp(Data[15])
            p[3]=p[3]+math.exp(Data[16])+math.exp(Data[17])+math.exp(Data[18])+math.exp(Data[19])+math.exp(Data[20])
            p[4]=p[4]+math.exp(Data[21])+math.exp(Data[22])+math.exp(Data[23])+math.exp(Data[24])+math.exp(Data[25])+math.exp(Data[26])   

        



