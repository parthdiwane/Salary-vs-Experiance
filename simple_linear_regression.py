# importing needed libraries 
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# reading the data 
dataset = pd.read_csv('salary_data.csv')
indep = dataset.iloc[:, :-1].values
dep = dataset.iloc[:,-1].values

# splitting the data into a test set and training set 
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(indep,dep, test_size = 0.2, random_state = 0)

# training the model using linear regression
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_train, y_train)

# predicts future test values, b/c we've only given the model 3 values 
# its going to use info from the training set 
y_pred = regressor.predict(x_test)

# visulizing training 
# red points = real salaries
# blue line = predicted salalries using the ML model 
plt.scatter(x_train,y_train, color = 'red') # plots points 
plt.plot(x_train, regressor.predict(x_train), color = 'blue') # plots a line
plt.title('Salary vs Experiance (Training Set)')
plt.xlabel('Years of Experiance')
plt.ylabel('Salary')
plt.show()

# visualizing the test set results
plt.scatter(x_test, y_test, color = 'red') # plots points 
plt.plot(x_train,regressor.predict(x_train), color = 'blue') # plots a line
plt.title('Salary vs Experiance (Test Set)')
plt.xlabel('Years of Experiance')
plt.ylabel('Salary')
plt.show()
