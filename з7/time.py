import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

alpha = 0.24

data = pd.read_csv('з7/task5.csv')
data.index += 1

def exponential_smoothing(series, alpha):
    result = [series[0]]
    for index in range(1, len(series)):
        result.append(alpha * series[index] + (1 - alpha) * result[index - 1]) 
    return result


data['y_exp_norm_user'] = exponential_smoothing(data['y'].to_list(), alpha)


print(f"значение 58-ой строки {data.loc[58]['y_exp_norm_user']}")

print(f"значение 100-ой строки {data.loc[100]['y_exp_norm_user']}")


X = data.index.to_numpy()
y = data['y'].to_numpy()
poly = np.polyfit(X, y, 1)
x = np.arange(1, 101)
a = round(poly[0], 2)
b = round(poly[1], 2)
data['lin_trend'] = a * x + b

plt.figure(figsize=(20, 8))
plt.plot('y', data=data)
plt.plot('lin_trend', data=data)
plt.xlabel('Time step')
plt.ylabel('y')
plt.show()

f_i = data['lin_trend']
y_avg = data['y'].mean()
R2 = 1 - ((y - f_i) ** 2).sum() / ((y - y_avg) ** 2).sum()

print(f"коэффицент a: {a}")
print(f"коэффицент R2: {round(R2, 3)}")
print(f"101-ый член ряда: {a * 101 + b}")