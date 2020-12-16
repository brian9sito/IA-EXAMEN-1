# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 16:59:43 2020

@author: BriaN
"""


import pandas as pd
from scipy.interpolate import interp1d
from matplotlib import pyplot as plt
import numpy as np
base =pd.read_csv('base.csv',header=0,delim_whitespace=0)
base['DEPARTAMENTO'].replace(['La Paz','Oruro','Cochabamba','Tarija','Beni','Chuquisaca'],[0,1,2,3,4,5],inplace=True)
base.drop(['NOMBRE COMPLETO', 'CI'],axis=1)
base['SEXO'].replace(['F','M'],[0,1],inplace=True)
#print(base)


x = np.array(base['NOTA PROMEDIO'])
y = np.array(base['EDAD'])
print(x)
print(y)
plt.plot(x,y,'bo')
plt.ylabel("EDAD")
plt.xlabel("Nota Promedio")
plt.show




