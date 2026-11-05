import numpy as np
import pandas as pd
from sklearn.cluster import KMeans


DATA = pd.read_csv("з17/data.csv", delimiter=',', index_col='Object')
coords = DATA.drop('Cluster', axis=1)

centroid = np.array([[11.6, 12.4], [12.13, 9.13], [1.5, 18.0]])

kmeans = KMeans(n_clusters=3, init=centroid, max_iter=100, n_init=1)

model = kmeans.fit(coords)
clusters = pd.DataFrame(coords)
clusters['Cluster'] = model.labels_.tolist()
print(clusters)
centrCoords = pd.DataFrame(coords)
centrCoords = centrCoords.reset_index(drop=True)
alldistances = kmeans.fit_transform(centrCoords)
closest_distances = alldistances[np.arange(len(centrCoords)), kmeans.labels_]
clusters['closest'] = closest_distances
print(clusters)
dist = clusters[clusters['Cluster'] == 0]

print("среднее расстояние до центроида кластер 0:", np.mean(dist['closest']))