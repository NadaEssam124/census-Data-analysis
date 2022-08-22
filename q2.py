# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 14:06:13 2022

@author: NADA ESSAM
"""

import pandas as pd


data=pd.read_csv('D:\\census_income_original_2.csv')

m=0
f=0

data['Gender']=data['Gender'].replace("M",'Male').replace("male",'Male').replace('malee','Male').replace('m','Male')
           
data['Gender']=data['Gender'].replace("f",'Female').replace("female",'Female')        
for i in (data['Gender']):
    if i=='Male':
      m=m+1
    else:
        f=f+1
    


print(m/(m+f)*100)
print(f/(m+f)*100)
print(data['Gender'].value_counts())



subset = data[['Gender','education','income']]

M = subset[data['Gender']=='Male'] #A
F = subset[data['Gender']=='Female']#B

print(m)
m_h=M[data['education']=='HS-grad']
print(m_h.value_counts())

f_h=F[data['education']=='HS-grad']
print(f_h.value_counts())

education= subset[data['education']=='Bachelors']
print(education.value_counts())



male_female_i=pd.DataFrame(data[['Gender','income']])
print(male_female_i.value_counts())




