#! usr/bin/python3
"""Author Oliver Tarrant
A model fitting script that fits an optimal mixture of poisson and negative binomial distributions to NGS data.
Requires 3 command line inputs:
    First input is an mpileup file with correct path to it's saved location
    Second input is the number of supercontigs file to be combined 
    Third input is the number of samples within the mpileup file that are wanted to be fitted
    Fourth input is the stem for the results file. This will be added to during the script to create seperate files for 
    the poisson and negative binomial distributions.
example running from terminal:
    python ../Data/example_mpileup 5 22 ../Results/example_results

    Running will result in the files ../Results/example_results_Poisson_data.csv & ../Results/example_results_Negative_Binomial_data.csv allong with 22 files of the form 
    ../Results/example_results_Model_Vals_Sample_i.csv each containing the values for of the fitted distributions for plotting purposes. 
    which will each contain the parameters of the optimally fitted model for each distribution respectively. 
"""
####Required packages for installation
import numpy as np # organising the data
import scipy as sc # Opperations such as percentile
import scipy.stats as scs # Statistical functions such as poisson distribution and percentiles
import pandas as pd # Creating and manipulating dataframes of results
import lmfit # Fitting the models to the data
import matplotlib.pyplot as plt # plotting the models fitted
import re # Read the results and extract the values
import sys # allow command line arguments of input and output files
import os # To subprocess the extraction of depth files from mpileup files



## determine input and ouput files
input = sys.argv[1]
Num_Supercontig=int(sys.argv[2])
NSAMS = int(sys.argv[3])
output = sys.argv[4]
print(input)

list_of_mpileups =[]
print("Converting mpileup file to depth files")
for m in range(Num_Supercontig):
    m=m+1 # deal with indexing
    mpileup = input+'.'+str(m)+'.mpileup'
    list_of_mpileups.append(mpileup)
    print("Found mpileup file: %s" % mpileup)
    #Convert = os.system('bash mpileup_depth.sh %s %s' %(mpileup,NSAMS))
    #if Convert==0:
    #	print("Conversion successful")
    #else: 
    #	print("Conversion failed")


#Define the mixture models to be fitted
print("Models to be fitted P1-5 and NB1-5")
    
######### Poisson mixture models ############
### see below for parameter definitions

def poisson_1(Poiss_Params):
    t=Poiss_Params.valuesdict()
    model_value=scs.poisson(t['mu1']).pmf(vals)
    residuals=model_value-actual
    return(residuals)
def poisson_2(Poiss_Params):
    t=Poiss_Params.valuesdict()
    model_value=(t['coef1'])*scs.poisson(t['mu1']).pmf(vals)+(1-t['coef1'])*scs.poisson(t['mu2']).pmf(vals)
    residuals=model_value-actual
    return(residuals)
def poisson_3(Poiss_Params):
    t=Poiss_Params.valuesdict()
    model_value=(t['coef1'])*scs.poisson(t['mu1']).pmf(vals)+(t['coef2'])*scs.poisson(t['mu2']).pmf(vals)+(1-t['coef1']-(t['coef2']))*scs.poisson(t['mu3']).pmf(vals)
    residuals=model_value-actual
    return(residuals)
def poisson_4(Poiss_Params):
    t=Poiss_Params.valuesdict()
    model_value=(t['coef1'])*scs.poisson(t['mu1']).pmf(vals)+(t['coef2'])*scs.poisson(t['mu2']).pmf(vals)+(t['coef3'])*scs.poisson(t['mu3']).pmf(vals)+(1-t['coef1']-t['coef2']-t['coef3'])*scs.poisson(t['mu4']).pmf(vals)
    residuals=model_value-actual
    return(residuals)
def poisson_5(Poiss_Params):
    t=Poiss_Params.valuesdict()
    model_value=(t['coef1'])*scs.poisson(t['mu1']).pmf(vals)+(t['coef2'])*scs.poisson(t['mu2']).pmf(vals)+(t['coef3'])*scs.poisson(t['mu3']).pmf(vals)+(t['coef4'])*scs.poisson(t['mu4']).pmf(vals)+(1-t['coef1']-t['coef2']-t['coef3']-t['coef4'])*scs.poisson(t['mu5']).pmf(vals)
    residuals=model_value-actual
    return(residuals)
########### Negative Binomial mixture models ############
### see below for parameter definitions

def neg_binomial_1(Neg_Binom_Params):
    u=Neg_Binom_Params.valuesdict()
    model_value=scs.nbinom(u['n1'],u['p1']).pmf(vals)
    residuals=model_value-actual
    return(residuals) 
def neg_binomial_2(Neg_Binom_Params):
    u=Neg_Binom_Params.valuesdict()
    model_value=(u['coef1'])*scs.nbinom(u['n1'],u['p1']).pmf(vals)+(1-u['coef1'])*scs.nbinom(u['n2'],u['p2']).pmf(vals)
    residuals=model_value-actual
    return(residuals) 
def neg_binomial_3(Neg_Binom_Params):
    u=Neg_Binom_Params.valuesdict()
    model_value=(u['coef1'])*scs.nbinom(u['n1'],u['p1']).pmf(vals)+(u['coef2'])*scs.nbinom(u['n2'],u['p2']).pmf(vals)+(1-u['coef1']-u['coef2'])*scs.nbinom(u['n3'],u['p3']).pmf(vals)
    residuals=model_value-actual
    return(residuals) 
def neg_binomial_4(Neg_Binom_Params):
    u=Neg_Binom_Params.valuesdict()
    model_value=(u['coef1'])*scs.nbinom(u['n1'],u['p1']).pmf(vals)+(u['coef2'])*scs.nbinom(u['n2'],u['p2']).pmf(vals)+(u['coef3'])*scs.nbinom(u['n3'],u['p3']).pmf(vals)+(1-u['coef1']-u['coef2']-u['coef3'])*scs.nbinom(u['n4'],u['p4']).pmf(vals)
    residuals=model_value-actual
    return(residuals) 
def neg_binomial_5(Neg_Binom_Params):
    u=Neg_Binom_Params.valuesdict()
    model_value=(u['coef1'])*scs.nbinom(u['n1'],u['p1']).pmf(vals)+(u['coef2'])*scs.nbinom(u['n2'],u['p2']).pmf(vals)+(u['coef3'])*scs.nbinom(u['n3'],u['p3']).pmf(vals)+(u['coef4'])*scs.nbinom(u['n4'],u['p4']).pmf(vals)+(1-u['coef1']-u['coef2']-u['coef3']-u['coef4'])*scs.nbinom(u['n5'],u['p5']).pmf(vals)
    residuals=model_value-actual
    return(residuals) 


   
#### Set up empty lists to store the required parameters from the best fitted models
Poiss_Actual=[]
Neg_Binom_Actual=[]
Better_Model=[]
Poiss_min=[]
Neg_Binom_min=[]
samples =[]


### For storage of resulting Poisson model parameters
MUS1_P=[]
MUS2_P=[]
MUS3_P=[]
MUS4_P=[]
MUS5_P=[]
COEF1_P=[]
COEF2_P=[]
COEF3_P=[]
COEF4_P=[]
COEF5_P=[]

### For storage of resulting Negative Binomial parameters
MUS1_NB=[]
MUS2_NB=[]
MUS3_NB=[]
MUS4_NB=[]
MUS5_NB=[]
COEF1_NB=[]
COEF2_NB=[]
COEF3_NB=[]
COEF4_NB=[]
COEF5_NB=[]
    

# Set up analysis for each gennome
for i in range(NSAMS): # study one sample at a time
    i = i+1 # deal with indexing
    samples.append("Sample %d" %i)
    print("Sample %d" %i)
    print("Compiling data")
    data = []
    for p in list_of_mpileups: # combine supercontigs 
        ### Determine level of data filtering 
        print("filtering depth file")
        temp=list(np.loadtxt('%s_depth_sample_%d.txt' %(p,i))) 
        length=str(len(temp))
        print("Pre-filtering length: %s" % length)
        upper = np.percentile(temp,90) 
        lower = np.percentile(temp,10)
        temp = list(filter(lambda x : x < upper and x > lower , temp)) # remove tails of data whilst preserving distribtuion shape
        length=str(len(temp))
        print("Post filtering length: %s" % length) 

        print("Adding depth file: %s_depth_sample_%d.txt" %(p,i)) 
        data.extend(temp) #Load the data
        print("Depth file %s_depth_sample_%d.txt succesfully added" %(p,i))
    
    
    

    Poiss=[]
    Neg_Binom=[]
    Poiss_Vals=[]
    Neg_Binom_Vals=[]
    
    print("Creating Parameters")    
    ##### take relevent part of each genome for analysis and add appropriate coeficient parameters
    Poiss_Params_1=lmfit.Parameters()
    Poiss_Params_1.add('mu1',value=np.percentile(data,50),min=1)
    print("P1 parameters created")  
    Poiss_Params_2=lmfit.Parameters()
    Poiss_Params_2.add('mu1',value=np.percentile(data,33),min=1)
    Poiss_Params_2.add('mu2',value=np.percentile(data,66),min=1)
    Poiss_Params_2.add('coef1',value=0.5,max=1,min=0.001)
    print("P2 parameters created")  
    Poiss_Params_3=lmfit.Parameters()
    Poiss_Params_3.add('mu1',value=np.percentile(data,25),min=1)
    Poiss_Params_3.add('mu2',value=np.percentile(data,50),min=1)
    Poiss_Params_3.add('mu3',value=np.percentile(data,75),min=1)
    Poiss_Params_3.add('coef1',value=0.3333,max=1,min=0.001)
    Poiss_Params_3.add('coef2',value=0.3333,max=1,min=0.001)
    print("P3 parameters created")  
    Poiss_Params_4=lmfit.Parameters()
    Poiss_Params_4.add('mu1',value=np.percentile(data,20),min=1)
    Poiss_Params_4.add('mu2',value=np.percentile(data,40),min=1)
    Poiss_Params_4.add('mu3',value=np.percentile(data,60),min=1)
    Poiss_Params_4.add('mu4',value=np.percentile(data,80),min=1)
    Poiss_Params_4.add('coef1',value=0.25,max=1,min=0.001)
    Poiss_Params_4.add('coef2',value=0.25,max=1,min=0.001)
    Poiss_Params_4.add('coef3',value=0.25,max=1,min=0.001)
    print("P4 parameters created")  
    Poiss_Params_5=lmfit.Parameters()
    Poiss_Params_5.add('mu1',value=np.percentile(data,16),min=1)
    Poiss_Params_5.add('mu2',value=np.percentile(data,33),min=1)
    Poiss_Params_5.add('mu3',value=np.percentile(data,49),min=1)
    Poiss_Params_5.add('mu4',value=np.percentile(data,66),min=1)
    Poiss_Params_5.add('mu5',value=np.percentile(data,84),min=1)
    Poiss_Params_5.add('coef1',value=0.2,max=1,min=0.001)
    Poiss_Params_5.add('coef2',value=0.2,max=1,min=0.001)
    Poiss_Params_5.add('coef3',value=0.2,max=1,min=0.001)
    Poiss_Params_5.add('coef4',value=0.2,max=1,min=0.001) 
    print("P5 parameters created")   
    Neg_Binom_Params_1=lmfit.Parameters()
    Neg_Binom_Params_1.add('n1',value=sum(data)/(40),min=1)
    Neg_Binom_Params_1.add('p1',value=1-np.percentile(data,50)/(sum(data)/(40)),min=0.001,max=1)
    print("NB1 parameters created")  
    Neg_Binom_Params_2=lmfit.Parameters()
    Neg_Binom_Params_2.add('n1',value=sum(data)/(2*40),min=1)
    Neg_Binom_Params_2.add('p1',value=1-np.percentile(data,33)/(sum(data)/(2*40)),min=0.001,max=1)
    Neg_Binom_Params_2.add('n2',value=sum(data)/(2*40),min=1)
    Neg_Binom_Params_2.add('p2',value=1-np.percentile(data,66)/(sum(data)/(2*40)),min=0.001,max=1)        
    Neg_Binom_Params_2.add('coef1',value=0.5,max=1,min=0.001)
    print("NB2 parameters created")  
    Neg_Binom_Params_3=lmfit.Parameters()
    Neg_Binom_Params_3.add('n1',value=sum(data)/(3*40),min=1)
    Neg_Binom_Params_3.add('p1',value=1-np.percentile(data,25)/(sum(data)/(3*40)),min=0.001,max=1)
    Neg_Binom_Params_3.add('n2',value=sum(data)/(3*40),min=1)
    Neg_Binom_Params_3.add('p2',value=1-np.percentile(data,50)/(sum(data)/(3*40)),min=0.001,max=1)
    Neg_Binom_Params_3.add('n3',value=sum(data)/(3*40),min=1)
    Neg_Binom_Params_3.add('p3',value=1-np.percentile(data,75)/(sum(data)/(3*40)),min=0.001,max=1)        
    Neg_Binom_Params_3.add('coef1',value=0.33,max=1,min=0.001)
    Neg_Binom_Params_3.add('coef2',value=0.33,max=1,min=0.001)
    print("NB3 parameters created")  
    Neg_Binom_Params_4=lmfit.Parameters()
    Neg_Binom_Params_4.add('n1',value=sum(data)/(4*40),min=1)
    Neg_Binom_Params_4.add('p1',value=1-np.percentile(data,20)/(sum(data)/(4*40)),min=0.001,max=1)
    Neg_Binom_Params_4.add('n2',value=sum(data)/(4*40),min=1)
    Neg_Binom_Params_4.add('p2',value=1-np.percentile(data,40)/(sum(data)/(4*40)),min=0.001,max=1)
    Neg_Binom_Params_4.add('n3',value=sum(data)/(4*40),min=1)
    Neg_Binom_Params_4.add('p3',value=1-np.percentile(data,60)/(sum(data)/(4*40)),min=0.001,max=1)
    Neg_Binom_Params_4.add('n4',value=sum(data)/(4*40),min=1)
    Neg_Binom_Params_4.add('p4',value=1-np.percentile(data,80)/(sum(data)/(4*40)),min=0.001,max=1)        
    Neg_Binom_Params_4.add('coef1',value=0.25,max=1,min=0.001)
    Neg_Binom_Params_4.add('coef2',value=0.25,max=1,min=0.001)
    Neg_Binom_Params_4.add('coef3',value=0.25,max=1,min=0.001)
    print("NB4 parameters created")  
    Neg_Binom_Params_5=lmfit.Parameters()
    Neg_Binom_Params_5.add('n1',value=sum(data)/(5*40),min=1)
    Neg_Binom_Params_5.add('p1',value=1-np.percentile(data,17)/(sum(data)/(5*40)),min=0.001,max=1)
    Neg_Binom_Params_5.add('n2',value=sum(data)/(5*40),min=1)
    Neg_Binom_Params_5.add('p2',value=1-np.percentile(data,33)/(sum(data)/(5*40)),min=0.001,max=1)
    Neg_Binom_Params_5.add('n3',value=sum(data)/(5*40),min=1)
    Neg_Binom_Params_5.add('p3',value=1-np.percentile(data,50)/(sum(data)/(5*40)),min=0.001,max=1)
    Neg_Binom_Params_5.add('n4',value=sum(data)/(5*40),min=1)
    Neg_Binom_Params_5.add('p4',value=1-np.percentile(data,67)/(sum(data)/(5*40)),min=0.001,max=1)
    Neg_Binom_Params_5.add('n5',value=sum(data)/(5*40),min=1)
    Neg_Binom_Params_5.add('p5',value=1-np.percentile(data,84)/(sum(data)/(5*40)),min=0.001,max=1)          
    Neg_Binom_Params_5.add('coef1',value=0.2,max=1,min=0.001)
    Neg_Binom_Params_5.add('coef2',value=0.2,max=1,min=0.001)
    Neg_Binom_Params_5.add('coef3',value=0.2,max=1,min=0.001)
    Neg_Binom_Params_5.add('coef4',value=0.2,max=1,min=0.001)
    print("NB5 parameters created")  
    ##### Organise data as required
    x = list(np.arange(int(min(data)),int(max(data)),1)) # Make list from min to max occurence step of 1
    vals=x
    y=[]    # set an empty list
    for j in x:
        y.append(data.count(j)/len(data))  # Add the proportions of the total count that match each value    
    actual=y
    
    print("Fitting")
    #### Fit the models #####
    try:
              
        Poiss_1_fit=lmfit.minimize(poisson_1,Poiss_Params_1)
        Poiss.append(lmfit.fit_report(Poiss_1_fit))
        Poiss_Vals.append(Poiss_1_fit.residual+actual)
        print("fit p1")
        counter1=1 # use counters to deal with exceptions for error handling
        Poiss_2_fit=lmfit.minimize(poisson_2,Poiss_Params_2)
        Poiss.append(lmfit.fit_report(Poiss_2_fit))
        Poiss_Vals.append(Poiss_2_fit.residual+actual)
        print("fit p2")
        counter1=2
        Poiss_3_fit=lmfit.minimize(poisson_3,Poiss_Params_3)
        Poiss.append(lmfit.fit_report(Poiss_3_fit))
        Poiss_Vals.append(Poiss_3_fit.residual+actual)
        print("fit p3")
        counter1=3
        Poiss_4_fit=lmfit.minimize(poisson_4,Poiss_Params_4)
        Poiss.append(lmfit.fit_report(Poiss_4_fit))
        Poiss_Vals.append(Poiss_4_fit.residual+actual)
        print("fit p4")
        counter1=4
        Poiss_5_fit=lmfit.minimize(poisson_5,Poiss_Params_5)
        Poiss.append(lmfit.fit_report(Poiss_5_fit))
        Poiss_Vals.append(Poiss_5_fit.residual+actual)
        print("fit p5")
        counter1=5
        Neg_Binom_1_fit =lmfit.minimize(neg_binomial_1,Neg_Binom_Params_1)
        Neg_Binom.append(lmfit.fit_report(Neg_Binom_1_fit))
        Neg_Binom_Vals.append(Neg_Binom_1_fit.residual+actual)
        print("fit NB1")
        counter2=1
        Neg_Binom_2_fit =lmfit.minimize(neg_binomial_2,Neg_Binom_Params_2)
        Neg_Binom.append(lmfit.fit_report(Neg_Binom_2_fit))
        Neg_Binom_Vals.append(Neg_Binom_2_fit.residual+actual)
        print("fit NB2")
        counter2=2
        Neg_Binom_3_fit =lmfit.minimize(neg_binomial_3,Neg_Binom_Params_3)
        Neg_Binom.append(lmfit.fit_report(Neg_Binom_3_fit))
        Neg_Binom_Vals.append(Neg_Binom_3_fit.residual+actual)
        print("fit NB3")
        counter2=3
        Neg_Binom_4_fit =lmfit.minimize(neg_binomial_4,Neg_Binom_Params_4)
        Neg_Binom.append(lmfit.fit_report(Neg_Binom_4_fit))
        Neg_Binom_Vals.append(Neg_Binom_4_fit.residual+actual)
        print("fit NB4")
        counter2=4
        Neg_Binom_5_fit =lmfit.minimize(neg_binomial_5,Neg_Binom_Params_5)
        Neg_Binom.append(lmfit.fit_report(Neg_Binom_5_fit))   
        Neg_Binom_Vals.append(Neg_Binom_5_fit.residual+actual)     
        print("fit NB5")
        counter2=5
    except (OSError,TypeError,ValueError):
        pass
    ### Determine which mixture model is best for each distribution 
    
    AIC_Poiss=[]
    AIC_Neg_Binom=[]

    for k in range(counter1):
        A_P = re.search('(Akaike\sinfo\scrit.*=\s)(.*)',Poiss[k])
        AIC_Poiss.append(float(A_P.group(2)))
    for k in range(counter2):
        A_NB = re.search('(Akaike\sinfo\scrit.*=\s)(.*)',Neg_Binom[k])
        AIC_Neg_Binom.append(float(A_NB.group(2)))
        
    ### Retrieve parameters for best model from the fit report.
    ### Ensuring if an error occured when fitting  model that the values for that ad more complex models not fitted are 0.
    Best_Poiss = AIC_Poiss.index(min(AIC_Poiss))
    Best_NB = AIC_Neg_Binom.index(min(AIC_Neg_Binom))
    if Best_Poiss == 4:
        M_1 = re.search('(\n\s*mu1:\s*)(\d*\.?\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Poiss[Best_Poiss])
        M_2 = re.search('(\n\s*mu2:\s*)(\d*\.?\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Poiss[Best_Poiss])
        M_3 = re.search('(\n\s*mu3:\s*)(\d*\.?\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Poiss[Best_Poiss])
        M_4 = re.search('(\n\s*mu4:\s*)(\d*\.?\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Poiss[Best_Poiss])
        M_5 = re.search('(\n\s*mu5:\s*)(\d*\.?\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Poiss[Best_Poiss])
        MUS1_P.append(float(M_1.group(2)))
        MUS2_P.append(float(M_2.group(2)))
        MUS3_P.append(float(M_3.group(2)))
        MUS4_P.append(float(M_4.group(2)))
        MUS5_P.append(float(M_5.group(2)))
        Co_1 = re.search('(\n\s*coef1:\s*)(\d*\.?\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Poiss[Best_Poiss]) 
        Co_2 = re.search('(\n\s*coef2:\s*)(\d*\.?\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Poiss[Best_Poiss]) 
        Co_3 = re.search('(\n\s*coef3:\s*)(\d*\.?\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Poiss[Best_Poiss]) 
        Co_4 = re.search('(\n\s*coef4:\s*)(\d*\.?\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Poiss[Best_Poiss]) 
        Co_5 = re.search('(\n\s*coef5:\s*)(\d*\.?\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Poiss[Best_Poiss])            
        COEF1_P.append(float(Co_1.group(2)))
        COEF2_P.append(float(Co_2.group(2)))
        COEF3_P.append(float(Co_3.group(2)))
        COEF4_P.append(float(Co_4.group(2)))
        COEF5_P.append(1-float(Co_1.group(2))-float(Co_2.group(2))-float(Co_3.group(2))-float(Co_4.group(2)))
    elif Best_Poiss == 3:
        M_1 = re.search('(\n\s*mu1:\s*)(\d*\.?\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Poiss[Best_Poiss])
        M_2 = re.search('(\n\s*mu2:\s*)(\d*\.?\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Poiss[Best_Poiss])
        M_3 = re.search('(\n\s*mu3:\s*)(\d*\.?\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Poiss[Best_Poiss])
        M_4 = re.search('(\n\s*mu4:\s*)(\d*\.?\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Poiss[Best_Poiss])
        
        MUS1_P.append(float(M_1.group(2)))
        MUS2_P.append(float(M_2.group(2)))
        MUS3_P.append(float(M_3.group(2)))
        MUS4_P.append(float(M_4.group(2)))
        MUS5_P.append(0)
        Co_1 = re.search('(\n\s*coef1:\s*)(\d*\.?\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Poiss[Best_Poiss]) 
        Co_2 = re.search('(\n\s*coef2:\s*)(\d*\.?\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Poiss[Best_Poiss]) 
        Co_3 = re.search('(\n\s*coef3:\s*)(\d*\.?\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Poiss[Best_Poiss]) 
        Co_4 = re.search('(\n\s*coef4:\s*)(\d*\.?\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Poiss[Best_Poiss]) 
               
        COEF1_P.append(float(Co_1.group(2)))
        COEF2_P.append(float(Co_2.group(2)))
        COEF3_P.append(float(Co_3.group(2)))
        COEF4_P.append(1-float(Co_1.group(2))-float(Co_2.group(2))-float(Co_3.group(2)))
        COEF5_P.append(0)
    elif Best_Poiss == 2:
        M_1 = re.search('(\n\s*mu1:\s*)(\d*\.?\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Poiss[Best_Poiss])
        M_2 = re.search('(\n\s*mu2:\s*)(\d*\.?\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Poiss[Best_Poiss])
        M_3 = re.search('(\n\s*mu3:\s*)(\d*\.?\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Poiss[Best_Poiss])
        MUS1_P.append(float(M_1.group(2)))
        MUS2_P.append(float(M_2.group(2)))
        MUS3_P.append(float(M_3.group(2)))
        MUS4_P.append(0)
        MUS5_P.append(0)
        Co_1 = re.search('(\n\s*coef1:\s*)(\d*\.?\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Poiss[Best_Poiss]) 
        Co_2 = re.search('(\n\s*coef2:\s*)(\d*\.?\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Poiss[Best_Poiss]) 
        Co_3 = re.search('(\n\s*coef3:\s*)(\d*\.?\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Poiss[Best_Poiss]) 
        COEF1_P.append(float(Co_1.group(2)))
        COEF2_P.append(float(Co_2.group(2)))
        COEF3_P.append(1-float(Co_1.group(2))-float(Co_2.group(2)))
        COEF4_P.append(0)
        COEF5_P.append(0)
    elif Best_Poiss == 1:
        M_1 = re.search('(\n\s*mu1:\s*)(\d*\.?\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Poiss[Best_Poiss])
        M_2 = re.search('(\n\s*mu2:\s*)(\d*\.?\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Poiss[Best_Poiss])
        MUS1_P.append(float(M_1.group(2)))
        MUS2_P.append(float(M_2.group(2)))
        MUS3_P.append(0)
        MUS4_P.append(0)
        MUS5_P.append(0)
        Co_1 = re.search('(\n\s*coef1:\s*)(\d*\.?\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Poiss[Best_Poiss]) 
        Co_2 = re.search('(\n\s*coef2:\s*)(\d*\.?\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Poiss[Best_Poiss])  
        COEF1_P.append(float(Co_1.group(2)))
        COEF2_P.append(1-float(Co_1.group(2)))
        COEF3_P.append(0)
        COEF4_P.append(0)
        COEF5_P.append(0)
    else:
        M_1 = re.search('(\n\s*mu1:\s*)(\d*\.?\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Poiss[Best_Poiss])
        MUS1_P.append(float(M_1.group(2)))
        MUS2_P.append(0)
        MUS3_P.append(0)
        MUS4_P.append(0)
        MUS5_P.append(0)
        Co_1 = re.search('(\n\s*coef1:\s*)(\d*\.?\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Poiss[Best_Poiss])  
        COEF1_P.append(1)
        COEF2_P.append(0)
        COEF3_P.append(0)
        COEF4_P.append(0)
        COEF5_P.append(0)           
    
    if Best_NB == 4:
        
        N_1 = re.search('(\n\s*n1:\s*)(\d*\.?\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Neg_Binom[Best_NB]) 
        N_2 = re.search('(\n\s*n2:\s*)(\d*\.?\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Neg_Binom[Best_NB]) 
        N_3 = re.search('(\n\s*n3:\s*)(\d*\.?\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Neg_Binom[Best_NB]) 
        N_4 = re.search('(\n\s*n4:\s*)(\d*\.?\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Neg_Binom[Best_NB]) 
        N_5 = re.search('(\n\s*n5:\s*)(\d*\.?\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Neg_Binom[Best_NB]) 
        P_1 = re.search('(\n\s*p1:\s*)(\d*\.?\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Neg_Binom[Best_NB]) 
        P_2 = re.search('(\n\s*p2:\s*)(\d*\.?\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Neg_Binom[Best_NB]) 
        P_3 = re.search('(\n\s*p3:\s*)(\d*\.?\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Neg_Binom[Best_NB]) 
        P_4 = re.search('(\n\s*p4:\s*)(\d*\.?\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Neg_Binom[Best_NB]) 
        P_5 = re.search('(\n\s*p5:\s*)(\d*\.?\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Neg_Binom[Best_NB])   
        MUS1_NB.append(scs.nbinom.mean(float(N_1.group(2)),float(P_1.group(2))))
        MUS2_NB.append(scs.nbinom.mean(float(N_2.group(2)),float(P_2.group(2))))
        MUS3_NB.append(scs.nbinom.mean(float(N_3.group(2)),float(P_3.group(2))))
        MUS4_NB.append(scs.nbinom.mean(float(N_4.group(2)),float(P_4.group(2))))
        MUS5_NB.append(scs.nbinom.mean(float(N_5.group(2)),float(P_5.group(2))))
        Co_1 = re.search('(\n\s*coef1:\s*)(\d*\.?\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Neg_Binom[Best_NB]) 
        Co_2 = re.search('(\n\s*coef2:\s*)(\d*\.?\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Neg_Binom[Best_NB]) 
        Co_3 = re.search('(\n\s*coef3:\s*)(\d*\.?\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Neg_Binom[Best_NB]) 
        Co_4 = re.search('(\n\s*coef4:\s*)(\d*\.?\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Neg_Binom[Best_NB]) 
        Co_5 = re.search('(\n\s*coef5:\s*)(\d*\.?\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Neg_Binom[Best_NB])            
        COEF1_NB.append(float(Co_1.group(2)))
        COEF2_NB.append(float(Co_2.group(2)))
        COEF3_NB.append(float(Co_3.group(2)))
        COEF4_NB.append(float(Co_4.group(2)))
        COEF5_NB.append(1-float(Co_1.group(2))-float(Co_2.group(2))-float(Co_3.group(2))-float(Co_4.group(2)))
    elif Best_NB == 3:
        
        N_1 = re.search('(\n\s*n1:\s*)(\d*\.?\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Neg_Binom[Best_NB]) 
        N_2 = re.search('(\n\s*n2:\s*)(\d*\.?\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Neg_Binom[Best_NB]) 
        N_3 = re.search('(\n\s*n3:\s*)(\d*\.?\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Neg_Binom[Best_NB]) 
        N_4 = re.search('(\n\s*n4:\s*)(\d*\.?\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Neg_Binom[Best_NB]) 
        P_1 = re.search('(\n\s*p1:\s*)(\d*\.?\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Neg_Binom[Best_NB]) 
        P_2 = re.search('(\n\s*p2:\s*)(\d*\.?\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Neg_Binom[Best_NB]) 
        P_3 = re.search('(\n\s*p3:\s*)(\d*\.?\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Neg_Binom[Best_NB]) 
        P_4 = re.search('(\n\s*p4:\s*)(\d*\.?\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Neg_Binom[Best_NB]) 
        MUS1_NB.append(scs.nbinom.mean(float(N_1.group(2)),float(P_1.group(2))))
        MUS2_NB.append(scs.nbinom.mean(float(N_2.group(2)),float(P_2.group(2))))
        MUS3_NB.append(scs.nbinom.mean(float(N_3.group(2)),float(P_3.group(2))))
        MUS4_NB.append(scs.nbinom.mean(float(N_4.group(2)),float(P_4.group(2))))
        MUS5_NB.append(0)
        Co_1 = re.search('(\n\s*coef1:\s*)(\d*\.?\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Neg_Binom[Best_NB]) 
        Co_2 = re.search('(\n\s*coef2:\s*)(\d*\.?\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Neg_Binom[Best_NB]) 
        Co_3 = re.search('(\n\s*coef3:\s*)(\d*\.?\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Neg_Binom[Best_NB]) 
        Co_4 = re.search('(\n\s*coef4:\s*)(\d*\.?\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Neg_Binom[Best_NB])            
        COEF1_NB.append(float(Co_1.group(2)))
        COEF2_NB.append(float(Co_2.group(2)))
        COEF3_NB.append(float(Co_3.group(2)))
        COEF4_NB.append(1-float(Co_1.group(2))-float(Co_2.group(2))-float(Co_3.group(2)))
        COEF5_NB.append(0)
    elif Best_NB == 2:
        
        N_1 = re.search('(\n\s*n1:\s*)(\d*\.?\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Neg_Binom[Best_NB]) 
        N_2 = re.search('(\n\s*n2:\s*)(\d*\.?\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Neg_Binom[Best_NB]) 
        N_3 = re.search('(\n\s*n3:\s*)(\d*\.?\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Neg_Binom[Best_NB]) 
        P_1 = re.search('(\n\s*p1:\s*)(\d*\.?\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Neg_Binom[Best_NB]) 
        P_2 = re.search('(\n\s*p2:\s*)(\d*\.?\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Neg_Binom[Best_NB]) 
        P_3 = re.search('(\n\s*p3:\s*)(\d*\.?\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Neg_Binom[Best_NB]) 
        MUS1_NB.append(scs.nbinom.mean(float(N_1.group(2)),float(P_1.group(2))))
        MUS2_NB.append(scs.nbinom.mean(float(N_2.group(2)),float(P_2.group(2))))
        MUS3_NB.append(scs.nbinom.mean(float(N_3.group(2)),float(P_3.group(2))))
        MUS4_NB.append(0)
        MUS5_NB.append(0)
        Co_1 = re.search('(\n\s*coef1:\s*)(\d*\.?\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Neg_Binom[Best_NB]) 
        Co_2 = re.search('(\n\s*coef2:\s*)(\d*\.?\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Neg_Binom[Best_NB]) 
        Co_3 = re.search('(\n\s*coef3:\s*)(\d*\.?\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Neg_Binom[Best_NB])           
        COEF1_NB.append(float(Co_1.group(2)))
        COEF2_NB.append(float(Co_2.group(2)))
        COEF3_NB.append(1-float(Co_1.group(2))-float(Co_2.group(2)))
        COEF4_NB.append(0)
        COEF5_NB.append(0)   
    elif Best_NB == 1:
        
        N_1 = re.search('(\n\s*n1:\s*)(\d*\.?\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Neg_Binom[Best_NB]) 
        N_2 = re.search('(\n\s*n2:\s*)(\d*\.?\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Neg_Binom[Best_NB])  
        P_1 = re.search('(\n\s*p1:\s*)(\d*\.?\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Neg_Binom[Best_NB]) 
        P_2 = re.search('(\n\s*p2:\s*)(\d*\.?\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Neg_Binom[Best_NB]) 
        MUS1_NB.append(scs.nbinom.mean(float(N_1.group(2)),float(P_1.group(2))))
        MUS2_NB.append(scs.nbinom.mean(float(N_2.group(2)),float(P_2.group(2))))
        MUS3_NB.append(0)
        MUS4_NB.append(0)
        MUS5_NB.append(0)
        Co_1 = re.search('(\n\s*coef1:\s*)(\d*\.?\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Neg_Binom[Best_NB]) 
        Co_2 = re.search('(\n\s*coef2:\s*)(\d*\.?\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Neg_Binom[Best_NB])            
        COEF1_NB.append(float(Co_1.group(2)))
        COEF2_NB.append(1-float(Co_1.group(2)))
        COEF3_NB.append(0)
        COEF4_NB.append(0)
        COEF5_NB.append(0)
    else:
        
        N_1 = re.search('(\n\s*n1:\s*)(\d*\.?\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Neg_Binom[Best_NB])  
        P_1 = re.search('(\n\s*p1:\s*)(\d*\.?\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Neg_Binom[Best_NB]) 
        MUS1_NB.append(scs.nbinom.mean(float(N_1.group(2)),float(P_1.group(2))))
        MUS2_NB.append(0)
        MUS3_NB.append(0)
        MUS4_NB.append(0)
        MUS5_NB.append(0)
        Co_1 = re.search('(\n\s*coef1:\s*)(\d*\.?\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Neg_Binom[Best_NB])            
        COEF1_NB.append(1)
        COEF2_NB.append(0)
        COEF3_NB.append(0)
        COEF4_NB.append(0)
        COEF5_NB.append(0)                       
    #### take basic stats on which model is best and compare
    Poiss_min.append(min(AIC_Poiss)) # minimum AIC value for the Poisson models
    Neg_Binom_min.append(min(AIC_Neg_Binom)) # minimum AIC value for the Negative Binomial models
    Best_Fit_Poiss=(AIC_Poiss.index(min(AIC_Poiss))+1) # Index of best fit model + 1 so that have the number of curves in best fitted model
    Poiss_Actual.append(Best_Fit_Poiss)
    Best_Fit_Neg_Binom=(AIC_Neg_Binom.index(min(AIC_Neg_Binom))+1) # Index of best fit model + 1 so that have the number of curves in best fitted model
    Neg_Binom_Actual.append(Best_Fit_Neg_Binom)
    #### extract lists of the fitted values of best distributions for plotting
    Poiss_1_Vals = list(Poiss_Vals[0])
    Poiss_2_Vals = list(Poiss_Vals[1])
    Poiss_3_Vals = list(Poiss_Vals[2])
    Poiss_4_Vals = list(Poiss_Vals[3])
    Poiss_5_Vals = list(Poiss_Vals[4])
    Poiss_Best_Model_Vals = list(Poiss_Vals[AIC_Poiss.index(min(AIC_Poiss))])
    Neg_Binom_1_Vals = list(Neg_Binom_Vals[0])
    Neg_Binom_2_Vals = list(Neg_Binom_Vals[1])
    Neg_Binom_3_Vals = list(Neg_Binom_Vals[2])
    Neg_Binom_4_Vals = list(Neg_Binom_Vals[3])
    Neg_Binom_5_Vals = list(Neg_Binom_Vals[4])
    Neg_Binom_Best_Model_Vals = list(Neg_Binom_Vals[AIC_Neg_Binom.index(min(AIC_Neg_Binom))])
    if min(AIC_Poiss)<min(AIC_Neg_Binom):
        Better_Model.append("P")
    elif min(AIC_Poiss)==min(AIC_Neg_Binom):
        Better_Model.append("T")
    else:
        Better_Model.append("NB")
        
    Model_Values={'X':x,'Actual':y,'Best Poisson':Poiss_Best_Model_Vals,'Best NB':Neg_Binom_Best_Model_Vals,'Poiss 1':Poiss_1_Vals,'Poiss 2':Poiss_2_Vals,'Poiss 3':Poiss_3_Vals,'Poiss 4':Poiss_4_Vals,'Poiss 5':Poiss_5_Vals,'Neg Binom 1':Neg_Binom_1_Vals,'Neg Binom 2':Neg_Binom_2_Vals,'Neg Binom 3':Neg_Binom_3_Vals,'Neg Binom 4':Neg_Binom_4_Vals,'Neg Binom 5':Neg_Binom_5_Vals}
    Mod_dfvals = pd.DataFrame.from_dict(Model_Values,orient='index')
    Mod_dfvals=Mod_dfvals.transpose()
    Mod_dfvals.to_csv('%s_Model_Vals_sample_%s.csv' % (output,i)) # provides data for example fitting plot


    
#### Output results to csv files to be analysed 

Res_Poisson={'Curves_Predicted':Poiss_Actual,'Minimum_AIC_value':Poiss_min,'Mu1':MUS1_P,'Mu2':MUS2_P,'Mu3':MUS3_P,'Mu4':MUS4_P,'Mu5':MUS5_P,'Coef1':COEF1_P,'Coef2':COEF2_P,'Coef3':COEF3_P,'Coef4':COEF4_P,'Coef5':COEF5_P}
Res_Negative_Binomial={'Curves_Predicted':Neg_Binom_Actual,'Minimum_AIC_value':Neg_Binom_min,'Mu1':MUS1_NB,'Mu2':MUS2_NB,'Mu3':MUS3_NB,'Mu4':MUS4_NB,'Mu5':MUS5_NB,'Coef1':COEF1_NB,'Coef2':COEF2_NB,'Coef3':COEF3_NB,'Coef4':COEF4_NB,'Coef5':COEF5_NB}
Res_Better_Model={'Better_Model':Better_Model}
Res_P_df=pd.DataFrame(Res_Poisson,index=samples)
Res_P_df=Res_P_df[['Curves_Predicted','Minimum_AIC_value','Mu1','Mu2','Mu3','Mu4','Mu5','Coef1','Coef2','Coef3','Coef4','Coef5']]
Res_P_df.to_csv('%s_Poisson_data.csv' % output)
Res_NB_df=pd.DataFrame(Res_Negative_Binomial,index=samples)
Res_NB_df=Res_NB_df[['Curves_Predicted','Minimum_AIC_value','Mu1','Mu2','Mu3','Mu4','Mu5','Coef1','Coef2','Coef3','Coef4','Coef5']]
Res_NB_df.to_csv('%s_Negative_Binomial_data.csv' % output)




print(Better_Model) # Shows if the optimal poisson or optimal negative binomial model was better 

# Refresh parameter so script can be looped for multiple mpileup files
Poiss_Params=lmfit.Parameters()
Neg_Binom_Params=lmfit.Parameters()
        