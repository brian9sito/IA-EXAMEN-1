# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 15:04:12 2020

@author: BriaN
"""
import matplotlib.pyplot as plt

import pandas as pd
import numpy as np
base =pd.read_csv('base.csv',header=0,delim_whitespace=0)

#------------Separamos NOTA PROMEDIO Y EDAD EN ARRAYS-------
y = np.array(base['NOTA PROMEDIO'])
z = np.array(base['EDAD'])
plt.xlabel("nota")
plt.ylabel("edad")
plt.plot(y,z,".")
plt.show()

#a)------LA MEDIA Y DESVIACION ESTANDAR DE LA NOTA PROMEDIO Y EDAD SIN LIBRERIAS-------------
print("---------------SIN LIBRERIAS-------------------------------------")
nn = len(y)
s=0
for i in range(nn):
    s = s + y[i]
mediaNOTA=s/nn
print("Media de la nota promedio")
print(mediaNOTA)

s=0
for i in range(nn):
    s = s + (y[i]-mediaNOTA)**2
print("Desviacion estandar")
print((s/nn)**0.5)
print("----------------------------------------------------")
ne = len(z)
s=0
for i in range(ne):
    s = s + z[i]
mediaEDAD=s/ne
print("Media de la edad")
print(mediaEDAD)
   
s=0
for i in range(ne):
    s = s + (z[i]-mediaEDAD)**2
print("Desviacion estandar de la edad")
print((s/ne)**0.5)

#b)-----La media, la moda, la desviación estándar con el uso de numpy y pandas------
print("------------------CON LIBRERIAS----------------------------------")
print("la media con numpy de notas")
print(np.mean(y))
print("la moda  de notas")
df=pd.DataFrame(y)
print(df.mode())
print("la desviacion estandar con numpy de notas")
print(np.std(y))

print("------------------------------------------------------")
print("la media con numpy de edad")
print(np.mean(z))
print("la moda  de edad")
df=pd.DataFrame(z)
print(df.mode())
print("la desviacion estandar con numpy de edad")
print(np.std(z))

