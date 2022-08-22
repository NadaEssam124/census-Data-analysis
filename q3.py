# -*- coding: utf-8 -*-
"""
Created on Sun Jul 31 23:19:48 2022

@author: NADA ESSAM
"""
import pandas as pd

data=pd.read_csv('D:\\census_income_original_2.csv')
#male_female_i=pd.DataFrame(data[['hours.per.week','income']])
#print(male_female_i.value_counts())


male_female_w=pd.DataFrame(data[0:100][['hours.per.week']])
male_female_i=pd.DataFrame(data[0:100][['income']])
print(male_female_w.mean())
print(male_female_i.value_counts())