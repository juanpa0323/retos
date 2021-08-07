# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 11:15:55 2021

@author: juanp
"""

import numpy as np
import pandas as pd
import numpy

df1=pd.read_csv("Poverty.csv",delimiter=",")
##print(df1)
##df1 = df1.replace(np.nan,"0")
df1['Population'].astype(float)
df1['MalePov18to24'].astype(float)
df1['MalePov25to34'].astype(float)
df1['FemalePov18to24'].astype(float)
df1['FemalePov25to34'].astype(float)
indices = ['a']
estado = df1["County"]
columnas = {'County':estado}
print("\n"*5)
print(type('County'))
print(df1['Population'],type(df1['Population']))
print(type('MalePov18to24'))
print(type('MalePov25to34'))
print(type('FemalePov18to24'))
print(type('FemalePov25to34'))
##,MalePov18to24,MalePov25to34,FemalePov18to24,FemalePov25to34

datos = pd.read_csv('Poverty.csv')
df = pd.DataFrame(datos)
df['Population'].astype(float)
print(type(df.loc[2,'Population']))
alto=df.loc[6,'MalePov25to34']
suma=3+alto
print(df.loc[6,'MalePov25to34'].dtype)
print(alto)
print(df.columns)
print(df.dtypes)
print(df.index)
print(suma)