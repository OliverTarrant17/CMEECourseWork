#! usr/bin/python3

"""Author Oliver Tarrant
A python script that takes an inputted text file of simulated ngs read data
and fits to it the best suited distribution.
"""
####Required packages for installation
import numpy as np # organising the data
import scipy as sc # Opperations such as percentile
import scipy.stats as scs # Statistical functions such as poisson distribution and percentiles
import pandas as pd # Creating and manipulating dataframes of results
import lmfit # Fitting the models to the data
import matplotlib.pyplot as plt # plotting the models fitted
import re # Read the results and extract the values
import os # to retrieve values from the bash script
import math # for mathematical operations like factorial and exponential

for q in [2,5,10,25,50,100]:
    data = list(np.loadtxt("../Data/First_Analysis/%s/depth.txt" % q )) #Load the data
    MEANDEPTH=q
    NSITES=int(len(data)/5)
        # Seperate the data into the seperate chromosomes
    chr1 = data[0:NSITES]
    chr2 = data[NSITES:2*NSITES]
    chr3 = data[2*NSITES:3*NSITES]
    chr4 = data[3*NSITES:4*NSITES]
    chr5 = data[4*NSITES:5*NSITES]
    chr = [chr1,chr2,chr3,chr4,chr5]
    
     
    
    x=[] # blank list of range from 0 to max for each chromosome
    for i in chr:
        x.append(list(np.arange(int(min(i))-1,int(max(i))+1,1))) # Make list from 1 to max occurence step of 1
        
    y=[]    # set an empty list
    k=0
    for i in x: # for each chromosome
            prop=[] # create a blank list for the proportions 
            for j in i: # the elements of the x[i]
    	            prop.append(chr[k].count(j)/len(chr[k]))  # Add the proportions of the total count that match each value of that chromosome
            y.append(prop) # add the proportions for each chromosome to the y list
            k=k+1 # move to next chromosome



   ############ Define the models and parameters 
    Poiss=list()
    R_sqrd_Poiss=list()
    Poiss_actual=list()
    Neg_Binom=list()
    R_sqrd_Neg_Binom=list()
    Neg_Binom_actual=list()
    Binom=list()
    Binom_actual=list()
    

######## Poisson #########

    def poisson(Poiss_Params):
        t=Poiss_Params.valuesdict()
        model_value=scs.poisson(t['mu']).pmf(vals)
        residuals=model_value-actual
        return(residuals)

######## Binomial ########

    def binomial(Binom_Params):
        v = Binom_Params.valuesdict()            
        model_value=scs.binom.pmf(vals,v['n'],v['p'])
        residuals=model_value-actual
        return(residuals)

######## Negative Binomial #########


    def neg_binomial(Neg_Binom_Params):
        u=Neg_Binom_Params.valuesdict()
        model_value=scs.nbinom(u['n'],u['prob']).pmf(vals)
        residuals=model_value-actual
        return(residuals) 

 

    
    try:
        for h in range(len(y)):
            ##### define chromosome specific values 
            vals=x[h]
            actual=y[h]
            approx_n = (sum(chr[h])/40) # n approximated using total occurances divided by the an approximate average read length
            approx_p = MEANDEPTH*(h+1)/approx_n
            ##### Set Parameters for the models
            Poiss_Params = lmfit.Parameters()
            Poiss_Params.add('mu',value=MEANDEPTH*(h+1),min=1)
            
            Binom_Params = lmfit.Parameters()
            Binom_Params.add('n', value=approx_n,min=0)  
            Binom_Params.add('p', value=approx_p,min=0,max=1)

            Neg_Binom_Params = lmfit.Parameters()
            Neg_Binom_Params.add('n',value=approx_n,min=1)
            Neg_Binom_Params.add('prob',value=1-approx_p,min=0.000000001,max=1)

            ###### Fit the models
            
            Poiss_fit=lmfit.minimize(poisson,Poiss_Params)
            Poiss.append(lmfit.fit_report(Poiss_fit))
            Poiss_actual.append(Poiss_fit.residual+actual)

            Binom_fit =lmfit.minimize(binomial,Binom_Params)
            Binom.append(lmfit.fit_report(Binom_fit))
            Binom_actual.append(Binom_fit.residual+actual)

            Neg_Binom_fit =lmfit.minimize(neg_binomial,Neg_Binom_Params)
            Neg_Binom.append(lmfit.fit_report(Neg_Binom_fit))
            Neg_Binom_actual.append(Neg_Binom_fit.residual+actual)
    except (OSError,TypeError,ValueError):
        raise

    
    Poiss_AIC=[]
    Poiss_BIC=[]
    Poiss_FUN=[]
    Poiss_CHI=[]
    Poiss_mu=[]
    Poiss_mu_err=[]
    Binom_AIC=[]
    Binom_BIC=[]
    Binom_FUN=[]
    Binom_CHI=[]
    Binom_n=[]
    Binom_n_err=[]
    Binom_p=[]
    Binom_p_err=[]
    Neg_Binom_AIC=[]
    Neg_Binom_BIC=[]
    Neg_Binom_FUN=[]
    Neg_Binom_CHI=[]
    Neg_Binom_n=[]
    Neg_Binom_n_err=[]
    Neg_Binom_prob=[]
    Neg_Binom_prob_err=[]
                # extract the required results
    
    for i in range(5):
        A = re.search('(Akaike\sinfo\scrit.*=\s)(.*)',Poiss[i])
        Poiss_AIC.append(float(A.group(2)))
        B = re.search('(Bayesian\sinfo\scrit.*=\s)(.*)',Poiss[i])
        Poiss_BIC.append(float(B.group(2)))
        funs = re.search('(function\sevals.*=\s)(.*)',Poiss[i])
        Poiss_FUN.append(float(funs.group(2)))
        chi = re.search('(\n\s*chi-square.*=\s)(.*)',Poiss[i])
        Poiss_CHI.append(float(chi.group(2)))
        mu = re.search('(\n\s*mu:\s*)(\d*\.\d*)(\s*\+/-\s*)(\d*.\d*)',Poiss[i])
        Poiss_mu.append(float(mu.group(2)))
        Poiss_mu_err.append(float(mu.group(4)))
            

        
        A = re.search('(Akaike\sinfo\scrit.*=\s)(.*)',Neg_Binom[i])
        Neg_Binom_AIC.append(float(A.group(2)))
        B = re.search('(Bayesian\sinfo\scrit.*=\s)(.*)',Neg_Binom[i])
        Neg_Binom_BIC.append(float(B.group(2)))
        funs = re.search('(function\sevals.*=\s)(.*)',Neg_Binom[i])
        Neg_Binom_FUN.append(float(funs.group(2)))
        chi = re.search('(\n\s*chi-square.*=\s)(.*)',Neg_Binom[i])
        Neg_Binom_CHI.append(float(chi.group(2)))
        n = re.search('(\n\s*n:\s*)(\d*\.\d*)(\s*\+/-\s*)(\d*.\d*)',Neg_Binom[i])
        Neg_Binom_n.append(float(mu.group(2)))
        Neg_Binom_n_err.append(float(mu.group(4)))
        prob = re.search('(\n\s*prob:\s*)(\d*\.\d*)(\s*\+/-\s*)(\d*.\d*)',Neg_Binom[i])
        Neg_Binom_prob.append(float(prob.group(2))) 
        Neg_Binom_prob_err.append(float(prob.group(4)))

        A = re.search('(Akaike\sinfo\scrit.*=\s)(.*)',Binom[i])
        Binom_AIC.append(float(A.group(2)))
        B = re.search('(Bayesian\sinfo\scrit.*=\s)(.*)',Binom[i])
        Binom_BIC.append(float(B.group(2)))
        funs = re.search('(function\sevals.*=\s)(.*)',Binom[i])
        Binom_FUN.append(float(funs.group(2)))
        chi = re.search('(\n\s*chi-square.*=\s)(.*)',Binom[i])
        Binom_CHI.append(float(chi.group(2)))
        n = re.search('(\n\s*n:\s*)(\d*\.\d*)(\s*\+/-\s*)(\d*.\d*)',Binom[i])
        Binom_n.append(float(mu.group(2)))
        Binom_n_err.append(float(mu.group(4)))
        p = re.search('(\n\s*p:\s*)(\d*\.\d*)(\s*\+/-\s*)(\d*.\d*)',Binom[i])
        Binom_p.append(float(p.group(2))) 
        Binom_p_err.append(float(p.group(4)))

    
    
    Poiss_Data={'AIC':Poiss_AIC,'BIC':Poiss_BIC,'Functions_evaluated':Poiss_FUN,'Chi-squared':Poiss_CHI,'Mu':Poiss_mu,'Mu_err':Poiss_mu_err}
    
    Binom_Data={'AIC':Binom_AIC,'BIC':Binom_BIC,'Functions_evaluated':Binom_FUN,'Chi-squared':Binom_CHI,'N':Binom_n,'N_err':Binom_n_err,
    'P':Binom_p,'P_err':Binom_p_err}

    Neg_Binom_Data={'AIC':Neg_Binom_AIC,'BIC':Neg_Binom_BIC,'Functions_evaluated':Neg_Binom_FUN,'Chi-squared':Neg_Binom_CHI,'N':Neg_Binom_n,'N_err':Neg_Binom_n_err,
    'P':Neg_Binom_prob,'P_err':Neg_Binom_prob_err}
    
    
    Poiss_df=pd.DataFrame(Poiss_Data,index=("1","2","3","4","5"))
    Binom_df=pd.DataFrame(Binom_Data,index=("1","2","3","4","5"))
    Neg_Binom_df=pd.DataFrame(Neg_Binom_Data,index=("1","2","3","4","5"))
    ## Reorder the dataframe columns
    Poiss_df=Poiss_df[['AIC','BIC','Functions_evaluated','Chi-squared','Mu','Mu_err']]
    Binom_df=Binom_df[['AIC','BIC','Functions_evaluated','Chi-squared','N','N_err','P','P_err']]
    Neg_Binom_df=Neg_Binom_df[['AIC','BIC','Functions_evaluated','Chi-squared','N','N_err','P','P_err']]
    
    ## Save the dataframes
    Poiss_df.to_csv('../Results/First_Analysis/%s/Poiss_Analysis_%s.csv' % (q,q))
    Binom_df.to_csv('../Results/First_Analysis/%s/Binom_Analysis_%s.csv' % (q,q))
    Neg_Binom_df.to_csv('../Results/First_Analysis/%s/Neg_Binom_Analysis_%s.csv' % (q,q))
    
    Poiss_Model_Values={'1':x[0],'Actual_1':y[0],'1_val':list(Poiss_actual[0]),'2':x[1],'Actual_2':y[1],'2_val':list(Poiss_actual[1]),'3':x[2],'Actual_3':y[2],'3_val':list(Poiss_actual[2]),'4':x[3],'Actual_4':y[3],'4_val':list(Poiss_actual[3]),'5':x[4],'Actual_5':y[4],'5_val':list(Poiss_actual[4])}
    P_dfvals = pd.DataFrame.from_dict(Poiss_Model_Values,orient='index')
    P_dfvals=P_dfvals.transpose()
    P_dfvals.to_csv('../Results/First_Analysis/%s/Poiss_Model_Vals_%s.csv' % (q,q))

    Binom_Model_Values={'1':x[0],'Actual_1':y[0],'1_val':list(Binom_actual[0]),'2':x[1],'Actual_2':y[1],'2_val':list(Binom_actual[1]),'3':x[2],'Actual_3':y[2],'3_val':list(Binom_actual[2]),'4':x[3],'Actual_4':y[3],'4_val':list(Binom_actual[3]),'5':x[4],'Actual_5':y[4],'5_val':list(Binom_actual[4])}
    B_dfvals = pd.DataFrame.from_dict(Binom_Model_Values,orient='index')
    B_dfvals=B_dfvals.transpose()
    B_dfvals.to_csv('../Results/First_Analysis/%s/Binom_Model_Vals_%s.csv' % (q,q))

    Neg_Binom_Model_Values={'1':x[0],'Actual_1':y[0],'1_val':list(Neg_Binom_actual[0]),'2':x[1],'Actual_2':y[1],'2_val':list(Neg_Binom_actual[1]),'3':x[2],'Actual_3':y[2],'3_val':list(Neg_Binom_actual[2]),'4':x[3],'Actual_4':y[3],'4_val':list(Neg_Binom_actual[3]),'5':x[4],'Actual_5':y[4],'5_val':list(Neg_Binom_actual[4])}
    NB_dfvals = pd.DataFrame.from_dict(Neg_Binom_Model_Values,orient='index')
    NB_dfvals=NB_dfvals.transpose()
    NB_dfvals.to_csv('../Results/First_Analysis/%s/Neg_Binom_Model_Vals_%s.csv' % (q,q))

print("Models finished fitting")
  
  
plt.plot(x[0],y[0],'go') #plot the data points
plt.plot(x[0],Poiss_Model_Values['1_val'],'r--', label="1Poisson") # plot initial fit
plt.plot(x[0],Binom_Model_Values['1_val'],'b--',label="1Binomial") # plot the best fit
plt.plot(x[0],Neg_Binom_Model_Values['1_val'],'y--', label="1Negative_Binomial") # plot initial fit

plt.plot(x[1],y[1],'go') #plot the data points
plt.plot(x[1],Poiss_Model_Values['2_val'],'r--', label="2Poisson") # plot initial fit
plt.plot(x[1],Binom_Model_Values['2_val'],'b--',label="2Binomial") # plot the best fit
plt.plot(x[1],Neg_Binom_Model_Values['2_val'],'y--', label="2Negative_Binomial") # plot initial fit

plt.plot(x[2],y[2],'go') #plot the data points
plt.plot(x[2],Poiss_Model_Values['3_val'],'r--', label="3Poisson") # plot initial fit
plt.plot(x[2],Binom_Model_Values['3_val'],'b--',label="3Binomial") # plot the best fit
plt.plot(x[2],Neg_Binom_Model_Values['3_val'],'y--', label="3Negative_Binomial") # plot initial fit

plt.plot(x[3],y[3],'go') #plot the data points
plt.plot(x[3],Poiss_Model_Values['4_val'],'r--', label="4Poisson") # plot initial fit
plt.plot(x[3],Binom_Model_Values['4_val'],'b--',label="4Binomial") # plot the best fit
plt.plot(x[3],Neg_Binom_Model_Values['4_val'],'y--', label="4Negative_Binomial") # plot initial fit

plt.plot(x[4],y[4],'go') #plot the data points
plt.plot(x[4],Poiss_Model_Values['5_val'],'r--', label="5Poisson") # plot initial fit
plt.plot(x[4],Binom_Model_Values['5_val'],'b--',label="5Binomial") # plot the best fit
plt.plot(x[4],Neg_Binom_Model_Values['5_val'],'y--', label="5Negative_Binomial") # plot initial fit

plt.legend()
#plt.show()