# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 23:43:18 2026

@author: Sanket
"""

# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Load the dataset
dataset = pd.read_csv(r"C:\Users\Sanket\AiWorkspace\MachineLearning\LinearRegression\Salary_Data.csv")
# Check the shape of the dataset
print("Dataset Shape:", dataset.shape)  # (30, 2)

#1. Feature selection (independent variable X and dependent variable y)
x = dataset.iloc[:, :-1]  # Years of experience (Independent variable)
y = dataset.iloc[:, -1]   # Salary (Dependent variable)

#Validate if there isany NaN or null values in the dataset. to check we can use console command
#dataset.isnull().sum() 
#output:
#    YearsExperience    0
#    Salary             0
#    dtype: int64
#So no Null or NaN values


# Split the dataset into training and testing sets (80% training, 20% testing)
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20,random_state=0)
#Here we provided test_size .20 so it consider train_size 0.8 & rancom_state make sure it use same data in every run for test and train

# Reshape x_train and x_test into 2D arrays if they are single feature columns
#x_train = x_train.values.reshape(-1, 1)
#x_test = x_test.values.reshape(-1, 1)

# You don't need to reshape y_train, as it's the target variable
# Fit the Linear Regression model to the training set
from sklearn.linear_model import LinearRegression #LinearRegression is algorith
regressor = LinearRegression()      #regressor is model since this object is turned into model
regressor.fit(x_train, y_train)

# Predicting the results for the test set
y_pred = regressor.predict(x_test)

# Visualizing the Training set results
plt.scatter(x_train, y_train, color = 'red')  # Real salary data (training)
plt.plot(x_train, regressor.predict(x_train), color = 'blue')  # Predicted regression line
plt.title('Salary vs Experience (Training set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

# Visualizing the Test set results
plt.scatter(x_test, y_test, color = 'red')  # Real salary data (testing)
plt.plot(x_train, regressor.predict(x_train), color = 'blue')  # Regression line from training set
plt.title('Salary vs Experience (Test set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

#In our dataset we have max experiance is of 10 years and its salary
#But if we want to predict the salary of 15year experianced based on the data provided?
#We can use following validation approach

#1. Calculate M of C=mx+c
m_slope = regressor.coef_
print(m_slope)  #[9312.57512673]

#2 Calculate C
c_intercept = regressor.intercept_
print(c_intercept)      #26780.09915062818

# Here x = 15 since we need to predict salary of 15 year experiance
#Fill values into c=mx+c and calculate predicted value.

year_15 = m_slope * 15 + c_intercept
print(year_15)      #Prediction is 166468.72605157


year_20 = m_slope * 20 + c_intercept
print(year_20)      #Prediction is 213031.60168521
