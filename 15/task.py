from sklearn.preprocessing import LabelEncoder
from sklearn.svm import LinearSVC
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from IPython.display import Image
from imutils import paths
import numpy as np
import cv2
import os
from sklearn.metrics import f1_score

def extract_histogram(image, bins=(8, 8, 8)):
    hist = cv2.calcHist([image], [0, 1, 2], None, bins, [0, 256, 0, 256, 0, 256])
    cv2.normalize(hist, hist)
    return hist.flatten()



imagePaths = sorted(list(paths.list_images('15\\train')))
data = []
labels = []

for (i, imagePath) in enumerate(imagePaths):
    image = cv2.imread(imagePath, 1)
    label = imagePath.split(os.path.sep)[-1].split(".")[0]
    hist = extract_histogram(image)
    data.append(hist)
    labels.append(label)

le = LabelEncoder()
labels = le.fit_transform(labels)


(trainData, testData, trainLabels, testLabels) = train_test_split(np.array(data), labels, test_size=25, random_state=2)
model = LinearSVC(random_state = 2, C = 0.94)
model.fit(trainData, trainLabels)
predictions = model.predict(testData)
print(classification_report(testLabels, predictions, target_names=le.classes_))


f1_score(testLabels, predictions, average='macro')

print("коэффициент:", model.coef_[0][0])


singleImage = cv2.imread('15\\test\\dog.1033.jpg')
histt = extract_histogram(singleImage)
histt2 = histt.reshape(1, -1)
prediction = model.predict(histt2)
print("предсказание dog.1033.jpg", prediction)

singleImage = cv2.imread('15\\test\\cat.1030.jpg')
histt = extract_histogram(singleImage)
histt2 = histt.reshape(1, -1)
prediction = model.predict(histt2)
print("предсказание cat.1030.jpg", prediction)

singleImage = cv2.imread('15\\test\\dog.1006.jpg')
histt = extract_histogram(singleImage)
histt2 = histt.reshape(1, -1)
prediction = model.predict(histt2)
print("предсказание dog.1006.jpg", prediction)

singleImage = cv2.imread('15\\test\\cat.1024.jpg')
histt = extract_histogram(singleImage)
histt2 = histt.reshape(1, -1)
prediction = model.predict(histt2)
print("предсказание cat.1024.jpg", prediction)