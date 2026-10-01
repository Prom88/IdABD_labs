import pandas as pd
import numpy as np

data = pd.read_csv('з6/task4.csv', index_col = 'ID')
data = 1 - np.exp(1 - data/data.min())

data['SUM'] = 0
data['SUM'] = data['DISTANCE'] + data['STOP_COUNT'] + data['COST']

bests = data.sort_values(by = ['SUM']).head(3)
bests = bests.index.to_list()

print(bests)