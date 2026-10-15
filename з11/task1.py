import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

data = pd.read_csv('з11/data.csv')
data.index +=1

X = pd.DataFrame(data.drop(['id', 'Y'], axis=1))
Y = pd.DataFrame(data['Y'])


reg = LinearRegression().fit(X, Y)
y_pred = reg.predict(X)



print("среднее:", y_pred.mean())
print("коэффицент:", reg.intercept_)
print("оценка точности:", reg.score(X, Y))