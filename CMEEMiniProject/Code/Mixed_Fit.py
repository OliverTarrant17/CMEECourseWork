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
    Better_Model=[]
    Poiss_min=[]
    Neg_Binom_min=[]
    Poiss_Vals=[]
    Neg_Binom_Vals=[]






        
        # Set up analysis for each gennome
    for i in np.arange(1,501):
        data = list(np.loadtxt("../Data/Second_Analysis/%s/mix_depth_%s.txt" % (MEANDEPTH,i) )) #Load the data
        Poiss=[]
        Neg_Binom=[]
        
        if i<101:
            Expected.append(1)
            
        elif i<201:
            Expected.append(2)   
        elif i<301:
            Expected.append(3) 
        elif i<401:
            Expected.append(4)
        else:
            Expected.append(5)    


            
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
        
        print("Fitting %s depth %s" % (i,MEANDEPTH))
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
    
    





        # set up arrays for results of the fits
        AIC_Poiss=[]
        AIC_Neg_Binom=[]



    
        for k in range(counter1):
            A_P = re.search('(Akaike\sinfo\scrit.*=\s)(.*)',Poiss[k])
            AIC_Poiss.append(float(A_P.group(2)))
        for k in range(counter2):
            A_NB = re.search('(Akaike\sinfo\scrit.*=\s)(.*)',Neg_Binom[k])
            AIC_Neg_Binom.append(float(A_NB.group(2)))


        
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
    
    Res_Poisson={'Predicted':Expected,'Actual':Poiss_Actual,'Minimum_value':Poiss_min}
    Res_Negative_Binomial={'Predicted':Expected,'Actual':Neg_Binom_Actual,'Minimum_value':Neg_Binom_min}
    Res_Better_Model={'Better_Model':Better_Model}
    Res_P_df=pd.DataFrame(Res_Poisson)
    Res_P_df.to_csv('../Results/Second_Analysis/Poisson_Confusion_data_%s.csv' % MEANDEPTH)
    Res_NB_df=pd.DataFrame(Res_Negative_Binomial)
    Res_NB_df.to_csv('../Results/Second_Analysis/Negative_Binomial_Confusion_data_%s.csv' % MEANDEPTH)
    Res_BM_df=pd.DataFrame(Res_Better_Model)
    Res_BM_df.to_csv('../Results/Second_Analysis/Better_Model_%s.csv' % MEANDEPTH)


    Model_Values={'X':x,'Actual':y,'P_val':list(Poiss_Vals[AIC_Poiss.index(min(AIC_Poiss))]),'NB_val':list(Neg_Binom_Vals[AIC_Neg_Binom.index(min(AIC_Neg_Binom))])}
    P_dfvals = pd.DataFrame.from_dict(Model_Values,orient='index')
    P_dfvals=P_dfvals.transpose()
    P_dfvals.to_csv('../Results/Second_Analysis/Model_Vals_%s.csv' % (MEANDEPTH)) # Provides data for example fitting plot


    Poiss_Params=lmfit.Parameters()
    Neg_Binom_Params=lmfit.Parameters()
    