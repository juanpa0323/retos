# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 12:38:25 2021

@author: juanp
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 18:44:47 2021

@author: juanp
"""
import pandas as pd
import numpy as np
df = pd.read_csv("titanic.csv")
print("DataFrame: \n",df)
dfshape=df.shape
print("Dimensión: Filas - Columnas",dfshape)
dfsize= df.size
print("Total datos: ",dfsize)
dfdtypes = df.dtypes
print("Nombre de las columnas y el tipo de dato; ",dfdtypes)
dfiloc = df.iloc[0:10]
print("Primeras 10 filas: \n",dfiloc)
dftail=df.tail(10)
print("Ultimas 10 filas: \n",dftail)
pasajero148 = df.loc[df['PassengerId']==148] 
print("Pasajero 148:\n",pasajero148)
print("Filas pares:\n")
fPares =  df.loc[df['PassengerId'] %2==0] 
fImpares = df.loc[df['PassengerId'] %2 !=0] 
###Mostrar por pantalla los nombres de las personas que iban en primera 
#clase ordenadas alfabéticamente.
#df.set_index("PassengerId",inplace=True)
p=df.loc[df['Pclass']==1,['Name']]
p = p.sort_values(by=['Name'])
#sort_values() El método de Pandas DataFrame. sort_values()
# ordena el llamador DataFrame en orden ascendente o descendente por los
# valores de la columna especificada a lo largo de cualquiera de los índices.
###Mostrar por pantalla el porcentaje de personas que sobrevivieron y murieron.
porcenSobrev=len(df[(df['Survived']==1)])/len(df.index)*100
porcenMurie=len(df[(df['Survived']==0)])/len(df.index)*100
print("El porcentaje de personas que sobrevivieron es de: ",round(porcenSobrev),"%")
print("El porcentaje de personas que murieron es de: ",round(porcenMurie),"%")        
###Mostrar por pantalla el porcentaje de personas que sobrevivieron en cada clase. 
sbc1=len(df[(df['Survived']==1) & (df['Pclass']==1)])/len(df.index)*100
sbc2=len(df[(df['Survived']==1) & (df['Pclass']==2)])/len(df.index)*100
sbc3=len(df[(df['Survived']==1) & (df['Pclass']==3)])/len(df.index)*100
print("% de sobrevivientes de primera clase: ",round(sbc1),"%")
print("% de sobrevivientes de  clase ejecutiva: ",round(sbc2),"%")
print("% de sobrevivientes de clase económica : ",round(sbc3),"%")
###8. Eliminar del DataFrame los pasajeros con edad desconocida. 
df = df[~np.isnan(df['Age'])]
EdadConocida=df
#9.	Mostrar por pantalla la edad media de las mujeres que viajaban en cada clase.
edadT =df[(df['Sex']=='female')]
edadMediaMujeres = edadT['Age'].sum()/len(edadT)
#10.	Añadir una nueva columna booleana para ver si el pasajero era menor de edad o no.
df['Menor'] = np.where(df['Age']<=18,True,False)

#11.	Mostrar por pantalla el porcentaje de menores y mayores de edad que 
#sobrevivieron en cada clase.
#despues de eliminar a las personas sin edad, el porcentaje de sobrevivientes cambia sería este:
#porcenSobrev1=len(df[(df['Survived']==1)])/len(df.index)*100
soMenores=len(df[(df['Survived']==1) & (df['Menor']==True)])/len(df.index)*100
soMayores=len(df[(df['Survived']==1) & (df['Menor']==False)])/len(df.index)*100