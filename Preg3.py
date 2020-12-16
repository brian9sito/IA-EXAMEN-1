# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 16:20:37 2020

@author: BriaN
"""
import pandas as pd
import numpy as np
bas =pd.read_csv('bas.csv',header=0)
bas['OBSERVACION'].replace([0,1],['reprobado','aprobado'],inplace=True)
print(bas)
bas_Train=pd.read_csv('bas_Train.csv',header=0)

#------------------Preprocesamiento-----------

bas=bas.drop(['NOMBRE COMPLETO', 'CI'],axis=1)
bas_Train=bas_Train.drop(['NOMBRE COMPLETO', 'CI'],axis=1)

bas['SEXO'].replace(['F','M'],[0,1],inplace=True)
bas_Train['SEXO'].replace(['F','M'],[0,1],inplace=True)
bas['DEPARTAMENTO'].replace(['La Paz','Oruro','Cochabamba','Tarija','Beni','Chuquisaca'],[0,1,2,3,4,5],inplace=True)
bas_Train['DEPARTAMENTO'].replace(['La Paz','Oruro','Cochabamba','Tarija','Beni','Chuquisaca'],[0,1,2,3,4,5],inplace=True)




from sklearn.model_selection import train_test_split
X = np.array(bas_Train.drop(['OBSERVACION'],1))
Y = np.array(bas_Train['OBSERVACION'])

X_train, X_test, Y_train, Y_test =train_test_split(X,Y,test_size=0.2)

from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier()
#modelo
model.fit(X_train, Y_train)
#predicción
print("prediccion")
print( model.predict(X_test))