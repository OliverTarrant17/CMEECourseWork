#! /usr/bin/python3

''' file to infer the critical values of delta likelihood to infer
 aneuploidy '''

import pandas as pd
import re
import matplotlib.pyplot as plty
import statsmodels.api as sm
import statsmodels.formula.api as smf
import numpy as np
from sklearn.preprocessing import OneHotEncoder

#import the data
Data=pd.read_csv('../Results/Interpret_delta',sep='\t',names=["Ploidies","Inferred_Ploidy","SNPs","Mean_read_depth","H_0","H_1","Delta","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20"])
# Create new column with normalised data
Data['Normalised_delta']=Data['Delta']/Data['SNPs']
Ploids=list(Data['Ploidies'])
base=[]
no_base=[]
aneu=[]
no_aneu=[]
is_aneu=[]
NSAMS=[]
for ploid in Ploids:
    ploid=re.split(',|x',ploid)
    base.append(int(ploid[0]))
    no_base.append(int(ploid[1]))
    aneu.append(int(ploid[2]))
    no_aneu.append(int(ploid[3]))
    if int(ploid[0])==int(ploid[2]):
        is_aneu.append(0)
    else:
        is_aneu.append(1)
    NSAMS.append(int(ploid[1])+int(ploid[3]))

Data['Base_ploidy']=base
Data['Base_ploidy_number']=no_base
Data['Aneuploidy_level']=aneu
Data['Number_of_aneuploidy']=no_aneu
Data['NSAMS']=NSAMS
Data['Aneuploidy']=is_aneu

Dependent_var=Data['Aneuploidy'].values
Independent_vars=Data[['Mean_read_depth','Inferred_Ploidy','SNPs','Normalised_delta']].values


#from sklearn.linear_model import LogisticRegression
#logistic=LogisticRegression()
#logistic.fit(Data[['Mean_read_depth']+['Inferred_Ploidy']+['SNPs']+['Normalised_delta']],Data[["Aneuploidy"]])
#predict1=logistic.predict(Data[['Mean_read_depth']+['Inferred_Ploidy']+['SNPs']+['Normalised_delta']])
#import numpy as np
#import matplotlib.pyplot as plt
#from sklearn import svm, datasets
#from sklearn.cross_validation import train_test_split
#from sklearn.metrics import confusion_matrix ###for using confusion matrix###
#cm1 = confusion_matrix(Data[['Aneuploidy']],predict1)
#print(cm1)
#total1=sum(sum(cm1))
#accuracy1=(cm1[0,0]+cm1[1,1])/total1
#accuracy1




#encode categorical data

onehotencoder=OneHotEncoder(categorical_features=[1])
Independent_vars=onehotencoder.fit_transform(Independent_vars).toarray()

Data1=Data.loc[lambda df:df.Inferred_Ploidy==1,:]
Data2=Data.loc[lambda df:df.Inferred_Ploidy==2,:]
Data3=Data.loc[lambda df:df.Inferred_Ploidy==3,:]
Data4=Data.loc[lambda df:df.Inferred_Ploidy==4,:]
Data5=Data.loc[lambda df:df.Inferred_Ploidy==5,:]

Data23=Data2.loc[lambda df:df.Aneuploidy_level==3,:]
Data23=Data23.reset_index(drop=True)
    



