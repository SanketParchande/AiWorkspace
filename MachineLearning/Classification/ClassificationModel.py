# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 23:40:57 2026

@author: Sanket
"""

import pandas as pd

dataset = pd.read_csv(r"C:\Users\Sanket\AiWorkspace\MachineLearning\Classification\Data.csv")

#Lets split the data in Independent variables and dependent variables
#x - IV
x = dataset.iloc[:, :-1].values

#y - DV : since its a binary variable we will be using classification algorithm
y = dataset.iloc[:,3].values

#Since IV has some null values in age and Salary colum we will beusing SKlearn framewok to fill those
#dataset.isnull().sum()
#Out[6]: 
#State        0
#Age          1
#Salary       1
#Purchased    0
#dtype: int64

#import sklearn

#Transformer for missing value: It just fill all the NaN values with mean strategy. 
#SimpleImputer helps us to fill the missing NaN or null values  using following strategies
from sklearn.impute import SimpleImputer

#Parameter Tuning
imputer = SimpleImputer() #mean strategy by default

#Hyper Parameter Tuning
#imputer = SimpleImputer(strategy="median") #this is Hyper  Parameter tuing

#Mode i.e most_frequent
#imputer = SimpleImputer(strategy="most_frequent")

imputer = imputer.fit(x[:,1:3]) #No transformation happens at this stage — it just learns and stores the statistics.
#print(imputer.statistics_) 
x[:,1:3]= imputer.transform(x[:,1:3]) # Apply the learned parameters to replace missing values in the data.
 

#machine learning framework preprocessing categorical data into numerical data
#we use the LabelEncoder
from sklearn.preprocessing import LabelEncoder
labelEnoder_x = LabelEncoder()
x[:,0] = labelEnoder_x.fit_transform(x[:,0])

#So far we have transormed  Independent variables to numerical form.
#Lets update Dependent variable purchase to numerical form now

labelEnoder_y = LabelEncoder()
y = labelEnoder_y.fit_transform(y)


#Step 6: Split dataset into Training data and Test Data
#x_train, x_test, y_train,y_test
#Lets split Train data to 80% and keep 20% test data
from sklearn.model_selection import train_test_split
x_train, x_test, y_train,y_test = train_test_split(x, y,test_size=0.2
                                                   ,train_size=0.8,random_state = 0)


