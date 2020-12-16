# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 15:56:23 2020

@author: BriaN
"""

import pandas as pd
import numpy as np
ub =pd.read_csv('ub2.csv',header=0)
print(ub)

#------------------Preprocesamiento-----------

ub=ub.drop(['Date','Origin Movement ID','Origin Display Name',
            'Destination Movement ID','Destination Display Name',
            'Daily Mean Travel Time (Seconds)','Daily Range - Lower Bound Travel Time (Seconds)',
            'Daily Range - Upper Bound Travel Time (Seconds)','AM Mean Travel Time (Seconds)',
            'AM Range - Lower Bound Travel Time (Seconds)','AM Range - Upper Bound Travel Time (Seconds)',
            'PM Mean Travel Time (Seconds)','PM Range - Lower Bound Travel Time (Seconds)',
            'PM Range - Upper Bound Travel Time (Seconds)','Midday Mean Travel Time (Seconds)',
            'Midday Range - Lower Bound Travel Time (Seconds)','Midday Range - Upper Bound Travel Time (Seconds)',
            'Evening Mean Travel Time (Seconds)'],axis=1)


from sklearn.impute import SimpleImputer
imp = SimpleImputer(missing_values=np.NaN, strategy='mean')
matriz_imputer = imp.fit_transform(ub)
print(matriz_imputer)

from sklearn.preprocessing import Normalizer
nor = Normalizer()
matriz_nor = nor.fit_transform(matriz_imputer)
print(matriz_nor)

from sklearn.preprocessing import StandardScaler
ssa = StandardScaler()
matriz_ssa = ssa.fit_transform(matriz_imputer)
print(matriz_ssa)


