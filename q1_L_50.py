# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 03:43:12 2022

@author: NADA ESSAM
"""

import pandas as pd

import matplotlib.pyplot as plt

#l<50k
data=pd.read_csv('D:\\census_income_original_2.csv')


data['income']=data['income'].replace("<=50K",0).replace(">50K",1)


subset = data[['age','income','capital.gain','capital.loss']]

# 1:split people acording to their income (<=50k or>50k)
l_50k = subset[data['income']==0] #A
g_50k = subset[data['income']==1]#B


# A.1:split people who their  income <=50k acording to capital gain


l_50k_l_c_g=l_50k[data['capital.gain']==0]
l_50k_g_c_g=l_50k[data['capital.gain']>0]

# A.1.1 split people who their  capital gain =0  acording to capital loss
less_c_loss_l_g=l_50k_l_c_g[data['capital.loss']==0]
greater_c_loss_l_g=l_50k_l_c_g[data['capital.loss']>0]

# A.1.2 split people who their  capital gain >0  acording to capital loss

less_c_loss_g_g=l_50k_g_c_g[data['capital.loss']==0]
greater_c_loss_g_g=l_50k_g_c_g[data['capital.loss']>0]



subset.plot(x='age', y = 'capital.gain', kind='scatter')
plt.show()
subset.plot(x='age', y = 'capital.loss', kind='scatter')
plt.show()
subset.plot(x='age', y = 'income', kind='scatter')
plt.show()

subset.mean().plot(kind='bar')

plt.show()

print(round(subset.mean()))
print(round(l_50k.mean()))
print(round(l_50k_l_c_g.mean()))
print(round(l_50k_g_c_g.mean()))

print(round(less_c_loss_l_g.mean()))
print(round(greater_c_loss_l_g.mean()))
print(round(less_c_loss_g_g.mean()))

