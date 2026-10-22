import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt


train_data = pd.read_csv("з12/Task_data.csv", delimiter=',')
X = pd.DataFrame(train_data.drop(['id', 'Class'], axis=1))

y = pd.DataFrame(train_data['Class']).values.ravel()


neighE = KNeighborsClassifier( metric='euclidean',
           n_neighbors=3, p=2)
neighE.fit(X, y)



newObj = pd.DataFrame([[74, 92]], columns=['X', 'Y'])

distances, indices = neighE.kneighbors(newObj)
print("Евклид:")
print('расстояние до ближайшего соседа:', distances.min())
print('Индексы соседей:', indices+1)
print('класс нового объекта:', neighE.predict(newObj))

neighM = KNeighborsClassifier( metric='manhattan',
           n_neighbors=3, p=2)
neighM.fit(X, y)

distances, indices = neighM.kneighbors(newObj)
print("Манхеттен:")
print('расстояние до ближайшего соседа:', distances.min())
print('Индексы соседей:', indices+1)
print('класс нового объекта:', neighM.predict(newObj))
