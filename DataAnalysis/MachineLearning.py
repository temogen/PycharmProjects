__author__ = 'Noventa'

import numpy as np
import pandas as pd
from pandas import Series, DataFrame


import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style('whitegrid')

from sklearn.datasets import load_boston

boston = load_boston()

print(boston.DESCR)

plt.hist(boston.target, bins=50)

plt.xlabel('Prices in $1000s')
plt.ylabel('Number of Houses')

plt.show()

plt.scatter(boston.data[:, 5], boston.target)


plt.ylabel('Price in $1000s')
plt.xlabel('Number of rooms')

boston_df = DataFrame(boston.data)

boston_df.columns = boston.feature_names

print(boston_df.head())

boston_df['Price'] = boston.target

boston_df.head()

sns.lmplot('RM', 'Price', data=boston_df)
plt.show()

X = boston_df.RM

X = np.vstack(boston_df.RM)

print(X.shape)

Y = boston_df.Price

X = np.array([value, 1] for value in X)

m, b = np.linalg.lstsq(X, Y)[0]

plt.plot(boston_df.RM, boston_df.Price, 'o')

x = boston_df.RM

plt.plot(x, m*x + b, 'r', label='Best Fit Line')

plt.show()

result = np.linalg.lstsq(X, Y)

error_total = result[1]
rmse = np.sqrt(error_total/len(X))

print('The root mean square error was %.2f' %rmse)

import sklearn
from sklearn.linear_model import LinearRegression

lreg = LinearRegression()
''' Linear Regressions() is an estimator '''

X_multi = boston_df.drop('Price', 1)
Y_target = boston_df.Price

lreg.fit(X_multi, Y_target)
print('The estimated intercept coefficient is %.2f ' %lreg.intercept_)
print('the number of coefficients used was %d' %len(lreg.coef))

coeff_df = DataFrame(boston_df.columns)
coeff_df.columns = ['Features']

coeff_df['Coefficient Estimate'] = pd.Series(lreg.coef_)
print(coeff_df)

