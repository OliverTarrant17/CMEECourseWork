#! usr/bin/python3
"""Author Oliver Tarrant
A python script that takes an inputted text file of simulated ngs read data
and fits it to an optimal mixture of possion distributions.
"""
####Required packages for installation
import numpy as np # organising the data
import scipy as sc # Opperations such as percentile
import scipy.stats as scs # Statistical functions such as poisson distribution and percentiles
import pandas as pd # Creating and manipulating dataframes of results
import lmfit # Fitting the models to the data
import matplotlib.pyplot as plt # plotting the models fitted
import re # Read the results and extract the values


    
#Define the mixture models to be fitted

    
######### Poisson mixture models ############

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


for MEANDEPTH in [2,5,10,25,50,100]:    
    Expected=[]
    Poiss_Actual=[]
    Neg_Binom_Actual=[]
    Poiss_Vals=[]
    Neg_Binom_Vals=[]
    Better_Model=[]
    Poiss_min=[]
    Neg_Binom_min=[]

    Num_1=[] ## number of chromosomes of each ploidy level
    Num_2=[]
    Num_3=[]
    Num_4=[]
    Num_5=[]
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
    for i in np.arange(1,101):
        data = list(np.loadtxt("../Data/Third_Analysis/%s/mix_depth_%s.txt" % (MEANDEPTH,i) )) #Load the data
        Poiss=[]
        Neg_Binom=[]
        

        Act_ploidies = list(np.loadtxt("../Data/Third_Analysis/%s/Genome_ploidy_%s.txt" %(MEANDEPTH,i)))   
        Num_1.append(Act_ploidies.count(1))
        Num_2.append(Act_ploidies.count(2))
        Num_3.append(Act_ploidies.count(3))
        Num_4.append(Act_ploidies.count(4))
        Num_5.append(Act_ploidies.count(5))
        Expected.append(len(set(Act_ploidies)))


            
        ##### take relevent part of each genome for analysis and add appropriate coeficient parameters

        Poiss_Params_1=lmfit.Parameters()
        Poiss_Params_1.add('mu1',value=np.percentile(data,50),min=1)

        Poiss_Params_2=lmfit.Parameters()
        Poiss_Params_2.add('mu1',value=np.percentile(data,33),min=1)
        Poiss_Params_2.add('mu2',value=np.percentile(data,66),min=1)
        Poiss_Params_2.add('coef1',value=0.5,max=1,min=0.001)

        Poiss_Params_3=lmfit.Parameters()
        Poiss_Params_3.add('mu1',value=np.percentile(data,25),min=1)
        Poiss_Params_3.add('mu2',value=np.percentile(data,50),min=1)
        Poiss_Params_3.add('mu3',value=np.percentile(data,75),min=1)
        Poiss_Params_3.add('coef1',value=0.3333,max=1,min=0.001)
        Poiss_Params_3.add('coef2',value=0.3333,max=1,min=0.001)

        Poiss_Params_4=lmfit.Parameters()
        Poiss_Params_4.add('mu1',value=np.percentile(data,20),min=1)
        Poiss_Params_4.add('mu2',value=np.percentile(data,40),min=1)
        Poiss_Params_4.add('mu3',value=np.percentile(data,60),min=1)
        Poiss_Params_4.add('mu4',value=np.percentile(data,80),min=1)
        Poiss_Params_4.add('coef1',value=0.25,max=1,min=0.001)
        Poiss_Params_4.add('coef2',value=0.25,max=1,min=0.001)
        Poiss_Params_4.add('coef3',value=0.25,max=1,min=0.001)
  
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


        Neg_Binom_Params_1=lmfit.Parameters()
        Neg_Binom_Params_1.add('n1',value=sum(data)/(40),min=1)
        Neg_Binom_Params_1.add('p1',value=1-np.percentile(data,50)/(sum(data)/(40)),min=0.001,max=1)

        Neg_Binom_Params_2=lmfit.Parameters()
        Neg_Binom_Params_2.add('n1',value=sum(data)/(2*40),min=1)
        Neg_Binom_Params_2.add('p1',value=1-np.percentile(data,33)/(sum(data)/(2*40)),min=0.001,max=1)
        Neg_Binom_Params_2.add('n2',value=sum(data)/(2*40),min=1)
        Neg_Binom_Params_2.add('p2',value=1-np.percentile(data,66)/(sum(data)/(2*40)),min=0.001,max=1)        
        Neg_Binom_Params_2.add('coef1',value=0.5,max=1,min=0.001)
        
        Neg_Binom_Params_3=lmfit.Parameters()
        Neg_Binom_Params_3.add('n1',value=sum(data)/(3*40),min=1)
        Neg_Binom_Params_3.add('p1',value=1-np.percentile(data,25)/(sum(data)/(3*40)),min=0.001,max=1)
        Neg_Binom_Params_3.add('n2',value=sum(data)/(3*40),min=1)
        Neg_Binom_Params_3.add('p2',value=1-np.percentile(data,50)/(sum(data)/(3*40)),min=0.001,max=1)
        Neg_Binom_Params_3.add('n3',value=sum(data)/(3*40),min=1)
        Neg_Binom_Params_3.add('p3',value=1-np.percentile(data,75)/(sum(data)/(3*40)),min=0.001,max=1)        
        Neg_Binom_Params_3.add('coef1',value=0.33,max=1,min=0.001)
        Neg_Binom_Params_3.add('coef2',value=0.33,max=1,min=0.001)

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


        ##### Organise data as required
        x = list(np.arange(int(min(data))-1,int(max(data))+1,1)) # Make list from min to max occurence step of 1
        vals=x
        y=[]    # set an empty list
        for j in x:
            y.append(data.count(j)/len(data))  # Add the proportions of the total count that match each value    
        actual=y
        
        print("Fitting %s" % i)
##### Fit the models #####
        try:
                  
            Poiss_1_fit=lmfit.minimize(poisson_1,Poiss_Params_1)
            Poiss.append(lmfit.fit_report(Poiss_1_fit))
            Poiss_Vals.append(Poiss_1_fit.residual+actual)
            print("fit p1")
            counter1=1
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
    
    




##### Determine which mixture model is best for each distribution 
        
        AIC_Poiss=[]
        AIC_Neg_Binom=[]
        for k in range(counter1):
            A_P = re.search('(Akaike\sinfo\scrit.*=\s)(.*)',Poiss[k])
            AIC_Poiss.append(float(A_P.group(2)))
        for k in range(counter2):
            A_NB = re.search('(Akaike\sinfo\scrit.*=\s)(.*)',Neg_Binom[k])
            AIC_Neg_Binom.append(float(A_NB.group(2)))
            


##### Retrieve parameters for best model
        Best_Poiss = AIC_Poiss.index(min(AIC_Poiss))
        Best_NB = AIC_Neg_Binom.index(min(AIC_Neg_Binom))
        if Best_Poiss == 4:
            M_1 = re.search('(\n\s*mu1:\s*)(\d*\.\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Poiss[Best_Poiss])
            M_2 = re.search('(\n\s*mu2:\s*)(\d*\.\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Poiss[Best_Poiss])
            M_3 = re.search('(\n\s*mu3:\s*)(\d*\.\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Poiss[Best_Poiss])
            M_4 = re.search('(\n\s*mu4:\s*)(\d*\.\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Poiss[Best_Poiss])
            M_5 = re.search('(\n\s*mu5:\s*)(\d*\.\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Poiss[Best_Poiss])
            MUS1_P.append(float(M_1.group(2)))
            MUS2_P.append(float(M_2.group(2)))
            MUS3_P.append(float(M_3.group(2)))
            MUS4_P.append(float(M_4.group(2)))
            MUS5_P.append(float(M_5.group(2)))
            Co_1 = re.search('(\n\s*coef1:\s*)(\d*\.\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Poiss[Best_Poiss]) 
            Co_2 = re.search('(\n\s*coef2:\s*)(\d*\.\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Poiss[Best_Poiss]) 
            Co_3 = re.search('(\n\s*coef3:\s*)(\d*\.\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Poiss[Best_Poiss]) 
            Co_4 = re.search('(\n\s*coef4:\s*)(\d*\.\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Poiss[Best_Poiss]) 
            Co_5 = re.search('(\n\s*coef5:\s*)(\d*\.\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Poiss[Best_Poiss])            
            COEF1_P.append(float(Co_1.group(2)))
            COEF2_P.append(float(Co_2.group(2)))
            COEF3_P.append(float(Co_3.group(2)))
            COEF4_P.append(float(Co_4.group(2)))
            COEF5_P.append(1-float(Co_1.group(2))-float(Co_2.group(2))-float(Co_3.group(2))-float(Co_4.group(2)))
        elif Best_Poiss == 3:
            M_1 = re.search('(\n\s*mu1:\s*)(\d*\.\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Poiss[Best_Poiss])
            M_2 = re.search('(\n\s*mu2:\s*)(\d*\.\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Poiss[Best_Poiss])
            M_3 = re.search('(\n\s*mu3:\s*)(\d*\.\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Poiss[Best_Poiss])
            M_4 = re.search('(\n\s*mu4:\s*)(\d*\.\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Poiss[Best_Poiss])
            
            MUS1_P.append(float(M_1.group(2)))
            MUS2_P.append(float(M_2.group(2)))
            MUS3_P.append(float(M_3.group(2)))
            MUS4_P.append(float(M_4.group(2)))
            MUS5_P.append(0)
            Co_1 = re.search('(\n\s*coef1:\s*)(\d*\.\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Poiss[Best_Poiss]) 
            Co_2 = re.search('(\n\s*coef2:\s*)(\d*\.\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Poiss[Best_Poiss]) 
            Co_3 = re.search('(\n\s*coef3:\s*)(\d*\.\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Poiss[Best_Poiss]) 
            Co_4 = re.search('(\n\s*coef4:\s*)(\d*\.\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Poiss[Best_Poiss]) 
                   
            COEF1_P.append(float(Co_1.group(2)))
            COEF2_P.append(float(Co_2.group(2)))
            COEF3_P.append(float(Co_3.group(2)))
            COEF4_P.append(1-float(Co_1.group(2))-float(Co_2.group(2))-float(Co_3.group(2)))
            COEF5_P.append(0)
        elif Best_Poiss == 2:
            M_1 = re.search('(\n\s*mu1:\s*)(\d*\.\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Poiss[Best_Poiss])
            M_2 = re.search('(\n\s*mu2:\s*)(\d*\.\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Poiss[Best_Poiss])
            M_3 = re.search('(\n\s*mu3:\s*)(\d*\.\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Poiss[Best_Poiss])
            MUS1_P.append(float(M_1.group(2)))
            MUS2_P.append(float(M_2.group(2)))
            MUS3_P.append(float(M_3.group(2)))
            MUS4_P.append(0)
            MUS5_P.append(0)
            Co_1 = re.search('(\n\s*coef1:\s*)(\d*\.\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Poiss[Best_Poiss]) 
            Co_2 = re.search('(\n\s*coef2:\s*)(\d*\.\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Poiss[Best_Poiss]) 
            Co_3 = re.search('(\n\s*coef3:\s*)(\d*\.\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Poiss[Best_Poiss]) 
            COEF1_P.append(float(Co_1.group(2)))
            COEF2_P.append(float(Co_2.group(2)))
            COEF3_P.append(1-float(Co_1.group(2))-float(Co_2.group(2)))
            COEF4_P.append(0)
            COEF5_P.append(0)
        elif Best_Poiss == 1:
            M_1 = re.search('(\n\s*mu1:\s*)(\d*\.\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Poiss[Best_Poiss])
            M_2 = re.search('(\n\s*mu2:\s*)(\d*\.\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Poiss[Best_Poiss])
            MUS1_P.append(float(M_1.group(2)))
            MUS2_P.append(float(M_2.group(2)))
            MUS3_P.append(0)
            MUS4_P.append(0)
            MUS5_P.append(0)
            Co_1 = re.search('(\n\s*coef1:\s*)(\d*\.\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Poiss[Best_Poiss]) 
            Co_2 = re.search('(\n\s*coef2:\s*)(\d*\.\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Poiss[Best_Poiss])  
            COEF1_P.append(float(Co_1.group(2)))
            COEF2_P.append(1-float(Co_1.group(2)))
            COEF3_P.append(0)
            COEF4_P.append(0)
            COEF5_P.append(0)
        else:
            M_1 = re.search('(\n\s*mu1:\s*)(\d*\.\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Poiss[Best_Poiss])
            MUS1_P.append(float(M_1.group(2)))
            MUS2_P.append(0)
            MUS3_P.append(0)
            MUS4_P.append(0)
            MUS5_P.append(0)
            Co_1 = re.search('(\n\s*coef1:\s*)(\d*\.\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Poiss[Best_Poiss])  
            COEF1_P.append(1)
            COEF2_P.append(0)
            COEF3_P.append(0)
            COEF4_P.append(0)
            COEF5_P.append(0)           
        
        if Best_NB == 4:
            
            N_1 = re.search('(\n\s*n1:\s*)(\d*\.\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Neg_Binom[Best_NB]) 
            N_2 = re.search('(\n\s*n2:\s*)(\d*\.\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Neg_Binom[Best_NB]) 
            N_3 = re.search('(\n\s*n3:\s*)(\d*\.\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Neg_Binom[Best_NB]) 
            N_4 = re.search('(\n\s*n4:\s*)(\d*\.\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Neg_Binom[Best_NB]) 
            N_5 = re.search('(\n\s*n5:\s*)(\d*\.\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Neg_Binom[Best_NB]) 
            P_1 = re.search('(\n\s*p1:\s*)(\d*\.\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Neg_Binom[Best_NB]) 
            P_2 = re.search('(\n\s*p2:\s*)(\d*\.\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Neg_Binom[Best_NB]) 
            P_3 = re.search('(\n\s*p3:\s*)(\d*\.\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Neg_Binom[Best_NB]) 
            P_4 = re.search('(\n\s*p4:\s*)(\d*\.\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Neg_Binom[Best_NB]) 
            P_5 = re.search('(\n\s*p5:\s*)(\d*\.\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Neg_Binom[Best_NB])   
            MUS1_NB.append(scs.nbinom.mean(float(N_1.group(2)),float(P_1.group(2))))
            MUS2_NB.append(scs.nbinom.mean(float(N_2.group(2)),float(P_2.group(2))))
            MUS3_NB.append(scs.nbinom.mean(float(N_3.group(2)),float(P_3.group(2))))
            MUS4_NB.append(scs.nbinom.mean(float(N_4.group(2)),float(P_4.group(2))))
            MUS5_NB.append(scs.nbinom.mean(float(N_5.group(2)),float(P_5.group(2))))

            Co_1 = re.search('(\n\s*coef1:\s*)(\d*\.\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Neg_Binom[Best_NB]) 
            Co_2 = re.search('(\n\s*coef2:\s*)(\d*\.\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Neg_Binom[Best_NB]) 
            Co_3 = re.search('(\n\s*coef3:\s*)(\d*\.\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Neg_Binom[Best_NB]) 
            Co_4 = re.search('(\n\s*coef4:\s*)(\d*\.\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Neg_Binom[Best_NB]) 
            Co_5 = re.search('(\n\s*coef5:\s*)(\d*\.\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Neg_Binom[Best_NB])            
            COEF1_NB.append(float(Co_1.group(2)))
            COEF2_NB.append(float(Co_2.group(2)))
            COEF3_NB.append(float(Co_3.group(2)))
            COEF4_NB.append(float(Co_4.group(2)))
            COEF5_NB.append(1-float(Co_1.group(2))-float(Co_2.group(2))-float(Co_3.group(2))-float(Co_4.group(2)))
        elif Best_NB == 3:
            
            N_1 = re.search('(\n\s*n1:\s*)(\d*\.\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Neg_Binom[Best_NB]) 
            N_2 = re.search('(\n\s*n2:\s*)(\d*\.\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Neg_Binom[Best_NB]) 
            N_3 = re.search('(\n\s*n3:\s*)(\d*\.\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Neg_Binom[Best_NB]) 
            N_4 = re.search('(\n\s*n4:\s*)(\d*\.\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Neg_Binom[Best_NB]) 
            P_1 = re.search('(\n\s*p1:\s*)(\d*\.\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Neg_Binom[Best_NB]) 
            P_2 = re.search('(\n\s*p2:\s*)(\d*\.\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Neg_Binom[Best_NB]) 
            P_3 = re.search('(\n\s*p3:\s*)(\d*\.\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Neg_Binom[Best_NB]) 
            P_4 = re.search('(\n\s*p4:\s*)(\d*\.\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Neg_Binom[Best_NB]) 
  
            MUS1_NB.append(scs.nbinom.mean(float(N_1.group(2)),float(P_1.group(2))))
            MUS2_NB.append(scs.nbinom.mean(float(N_2.group(2)),float(P_2.group(2))))
            MUS3_NB.append(scs.nbinom.mean(float(N_3.group(2)),float(P_3.group(2))))
            MUS4_NB.append(scs.nbinom.mean(float(N_4.group(2)),float(P_4.group(2))))
            MUS5_NB.append(0)

            Co_1 = re.search('(\n\s*coef1:\s*)(\d*\.\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Neg_Binom[Best_NB]) 
            Co_2 = re.search('(\n\s*coef2:\s*)(\d*\.\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Neg_Binom[Best_NB]) 
            Co_3 = re.search('(\n\s*coef3:\s*)(\d*\.\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Neg_Binom[Best_NB]) 
            Co_4 = re.search('(\n\s*coef4:\s*)(\d*\.\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Neg_Binom[Best_NB])            
            COEF1_NB.append(float(Co_1.group(2)))
            COEF2_NB.append(float(Co_2.group(2)))
            COEF3_NB.append(float(Co_3.group(2)))
            COEF4_NB.append(1-float(Co_1.group(2))-float(Co_2.group(2))-float(Co_3.group(2)))
            COEF5_NB.append(0)
        elif Best_NB == 2:
            
            N_1 = re.search('(\n\s*n1:\s*)(\d*\.\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Neg_Binom[Best_NB]) 
            N_2 = re.search('(\n\s*n2:\s*)(\d*\.\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Neg_Binom[Best_NB]) 
            N_3 = re.search('(\n\s*n3:\s*)(\d*\.\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Neg_Binom[Best_NB]) 
            P_1 = re.search('(\n\s*p1:\s*)(\d*\.\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Neg_Binom[Best_NB]) 
            P_2 = re.search('(\n\s*p2:\s*)(\d*\.\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Neg_Binom[Best_NB]) 
            P_3 = re.search('(\n\s*p3:\s*)(\d*\.\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Neg_Binom[Best_NB]) 

  
            MUS1_NB.append(scs.nbinom.mean(float(N_1.group(2)),float(P_1.group(2))))
            MUS2_NB.append(scs.nbinom.mean(float(N_2.group(2)),float(P_2.group(2))))
            MUS3_NB.append(scs.nbinom.mean(float(N_3.group(2)),float(P_3.group(2))))
            MUS4_NB.append(0)
            MUS5_NB.append(0)

            Co_1 = re.search('(\n\s*coef1:\s*)(\d*\.\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Neg_Binom[Best_NB]) 
            Co_2 = re.search('(\n\s*coef2:\s*)(\d*\.\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Neg_Binom[Best_NB]) 
            Co_3 = re.search('(\n\s*coef3:\s*)(\d*\.\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Neg_Binom[Best_NB])           
            COEF1_NB.append(float(Co_1.group(2)))
            COEF2_NB.append(float(Co_2.group(2)))
            COEF3_NB.append(1-float(Co_1.group(2))-float(Co_2.group(2)))
            COEF4_NB.append(0)
            COEF5_NB.append(0)   
        elif Best_NB == 1:
            
            N_1 = re.search('(\n\s*n1:\s*)(\d*\.\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Neg_Binom[Best_NB]) 
            N_2 = re.search('(\n\s*n2:\s*)(\d*\.\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Neg_Binom[Best_NB])  
            P_1 = re.search('(\n\s*p1:\s*)(\d*\.\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Neg_Binom[Best_NB]) 
            P_2 = re.search('(\n\s*p2:\s*)(\d*\.\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Neg_Binom[Best_NB]) 
            MUS1_NB.append(scs.nbinom.mean(float(N_1.group(2)),float(P_1.group(2))))
            MUS2_NB.append(scs.nbinom.mean(float(N_2.group(2)),float(P_2.group(2))))
            MUS3_NB.append(0)
            MUS4_NB.append(0)
            MUS5_NB.append(0)
            Co_1 = re.search('(\n\s*coef1:\s*)(\d*\.\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Neg_Binom[Best_NB]) 
            Co_2 = re.search('(\n\s*coef2:\s*)(\d*\.\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Neg_Binom[Best_NB])            
            COEF1_NB.append(float(Co_1.group(2)))
            COEF2_NB.append(1-float(Co_1.group(2)))
            COEF3_NB.append(0)
            COEF4_NB.append(0)
            COEF5_NB.append(0)
        else:
            
            N_1 = re.search('(\n\s*n1:\s*)(\d*\.\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Neg_Binom[Best_NB])  
            P_1 = re.search('(\n\s*p1:\s*)(\d*\.\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Neg_Binom[Best_NB]) 
            MUS1_NB.append(scs.nbinom.mean(float(N_1.group(2)),float(P_1.group(2))))
            MUS2_NB.append(0)
            MUS3_NB.append(0)
            MUS4_NB.append(0)
            MUS5_NB.append(0)
            Co_1 = re.search('(\n\s*coef1:\s*)(\d*\.\d*e?\+?\d*)(\s*\+/-\s*)(\d*.\d*e?\+?\d*)',Neg_Binom[Best_NB])            
            COEF1_NB.append(1)
            COEF2_NB.append(0)
            COEF3_NB.append(0)
            COEF4_NB.append(0)
            COEF5_NB.append(0)                       





#### take basic stats on which model is best and compare

        Poiss_min.append(min(AIC_Poiss))
        Neg_Binom_min.append(min(AIC_Neg_Binom))
        Best_Fit_Poiss=(AIC_Poiss.index(min(AIC_Poiss))+1)
        Poiss_Actual.append(Best_Fit_Poiss)
        Best_Fit_Neg_Binom=(AIC_Neg_Binom.index(min(AIC_Neg_Binom))+1)
        Neg_Binom_Actual.append(Best_Fit_Neg_Binom)
        if min(AIC_Poiss)<min(AIC_Neg_Binom):
            Better_Model.append("P")
        elif min(AIC_Poiss)==min(AIC_Neg_Binom):
            Better_Model.append("T")
        else:
            Better_Model.append("NB")
#### Output results to csv files to be analysed in R   
    Composition={'1':Num_1,'2':Num_2,'3':Num_3,'4':Num_4,'5':Num_5}
    Res_Poisson={'Predicted':Expected,'Actual':Poiss_Actual,'Minimum_value':Poiss_min,'Mu1':MUS1_P,'Mu2':MUS2_P,'Mu3':MUS3_P,'Mu4':MUS4_P,'Mu5':MUS5_P,'Coef1':COEF1_P,'Coef2':COEF2_P,'Coef3':COEF3_P,'Coef4':COEF4_P,'Coef5':COEF5_P}
    Res_Negative_Binomial={'Predicted':Expected,'Actual':Neg_Binom_Actual,'Minimum_value':Neg_Binom_min,'Mu1':MUS1_NB,'Mu2':MUS2_NB,'Mu3':MUS3_NB,'Mu4':MUS4_NB,'Mu5':MUS5_NB,'Coef1':COEF1_NB,'Coef2':COEF2_NB,'Coef3':COEF3_NB,'Coef4':COEF4_NB,'Coef5':COEF5_NB}
    Res_Better_Model={'Better_Model':Better_Model}
    Res_P_df=pd.DataFrame(Res_Poisson)
    Res_P_df.to_csv('../Results/Third_Analysis/Poisson_Confusion_data_%s.csv' % MEANDEPTH)
    Res_NB_df=pd.DataFrame(Res_Negative_Binomial)
    Res_NB_df.to_csv('../Results/Third_Analysis/Negative_Binomial_Confusion_data_%s.csv' % MEANDEPTH)
    Res_BM_df=pd.DataFrame(Res_Better_Model)
    Res_BM_df.to_csv('../Results/Third_Analysis/Better_Model_%s.csv' % MEANDEPTH)

    Model_Values={'X':x,'Actual':y,'P_val':list(Poiss_Vals[AIC_Poiss.index(min(AIC_Poiss))]),'NB_val':list(Neg_Binom_Vals[AIC_Neg_Binom.index(min(AIC_Neg_Binom))])}
    Mod_dfvals = pd.DataFrame.from_dict(Model_Values,orient='index')
    Mod_dfvals=Mod_dfvals.transpose()
    Mod_dfvals.to_csv('../Results/Third_Analysis/Model_Vals_%s.csv' % (MEANDEPTH)) # provides data for example fitting plot


    Poiss_Params=lmfit.Parameters()
    Neg_Binom_Params=lmfit.Parameters()
    