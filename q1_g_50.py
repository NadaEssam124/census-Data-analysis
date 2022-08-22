# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 03:10:53 2022

@author: NADA ESSAM
"""
import pandas as pd



data=pd.read_csv('D:\\census_income_original_2.csv')

avg_age=data['age'].mean()


data['income']=data['income'].replace("<=50K",0).replace(">50K",1)


subset = data[['age','income','capital.gain','capital.loss']]

# 1:split people acording to their income (<=50k or>50k)
l_50k = subset[data['income']==0] #A
g_50k = subset[data['income']==1]#B


# B.1:split people who their  income >50k acording to capital gain


g_50k_l_c_g=g_50k[data['capital.gain']==0]
g_50k_g_c_g=g_50k[data['capital.gain']>0]


# B.1.1 split people who their  capital gain =0  acording to capital loss
less_c_loss_l_g=g_50k_l_c_g[data['capital.loss']==0]
greater_c_loss_l_g=g_50k_l_c_g[data['capital.loss']>0]

# B.1.2 split people who their  capital gain >0  acording to capital loss

less_c_loss_g_g=g_50k_g_c_g[data['capital.loss']==0]
greater_c_loss_g_g=g_50k_g_c_g[data['capital.loss']>0]


print(round(g_50k.mean()))
print(round(g_50k_l_c_g.mean()))
print(round(g_50k_g_c_g.mean()))
print(round(less_c_loss_l_g.mean()))
print(round(greater_c_loss_l_g.mean()))
print(round(less_c_loss_g_g.mean()))











