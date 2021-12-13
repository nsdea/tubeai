import pandas as pd
from sklearn import linear_model
from  matplotlib import pyplot 
import numpy as np

#read data
x = np.random.rand(25,2)
x[:,1] = 2*x[:,0]+np.random.rand(25)
dataframe = pd.DataFrame(x,columns=['Brain','Body'])


x_values=dataframe['Brain'].values[:,np.newaxis]
y_values=dataframe['Body'].values[:,np.newaxis]

body_reg = linear_model.LinearRegression()
body_reg.fit(x_values, y_values)
prediction=body_reg.predict(np.sort(x_values, axis=0))

pyplot.scatter(x_values, y_values)
pyplot.plot(np.sort(x_values, axis=0),prediction)
pyplot.show()
