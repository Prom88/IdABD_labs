import pandas as pd
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz
import graphviz
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score


df = pd.read_csv('з16/diabetes.csv') 
task_data = df.head(590)
len(task_data[task_data['Outcome'] == 1])
train = task_data.head(int(len(task_data)*0.7))
test = task_data.tail(int(len(task_data)*0.3))
features = list(train.columns[:8])
x = train[features]
y = train['Outcome']
tree = DecisionTreeClassifier(criterion='entropy', #критерий разделения
                              min_samples_leaf=20, #минимальное число объектов в листе
                              max_leaf_nodes=30, #максимальное число листьев
                              random_state=2020)
clf=tree.fit(x, y)


columns = list(x.columns)
export_graphviz(clf, out_file='tree.dot', 
                feature_names=columns,
                class_names=['0', '1'],
                rounded = True, proportion = False, 
                precision = 2, filled = True, label='all')

with open('tree.dot') as f:
    dot_graph = f.read()

graphviz.Source(dot_graph)


features = list(test.columns[:8])
x = test[features]
y_true = test['Outcome']
y_pred = clf.predict(x)



print(accuracy_score(y_true, y_pred))
print(f1_score(y_true, y_pred, average='macro'))
print(clf.predict([df.loc[708, features].tolist()])[0])