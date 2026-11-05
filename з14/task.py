import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
import sklearn.metrics as scm


Data = pd.read_csv('з14/candy-data.csv', index_col='competitorname')
Test = pd.read_csv('з14/candy-test.csv', index_col='competitorname')


Data = Data.drop(['Chewey Lemonhead Fruit Mix', 'Runts', 'Sixlets'])


X = pd.DataFrame(Data.drop(['winpercent', 'Y'], axis=1))
Y = pd.DataFrame(Data['Y'])

model = LogisticRegression(random_state=2019, solver='lbfgs')

model.fit(X, np.ravel(Y))

YPredicted = model.predict(pd.DataFrame(Test.drop(['Y'], axis=1)))
YProbability = pd.DataFrame(model.predict_proba(pd.DataFrame(Test.drop(['Y'], axis=1))))
Test['Y_predicted'] = YPredicted
Test['Y_predicted_chance'] = YProbability[1].values

print("вероятность отнесения конфеты Sugar Babies к классу 1:", Test.loc["Sugar Babies"]["Y_predicted_chance"])
print("вероятность отнесения конфеты Whoppers к классу 1:", Test.loc["Whoppers"]["Y_predicted_chance"])

cm = scm.confusion_matrix(Test["Y"], Test["Y_predicted"], labels=None, sample_weight=None, normalize=None)
print("Матрица ошибок:", cm)
print("Recall:", scm.recall_score(Test["Y"], Test["Y_predicted"]))
print("Precision:", scm.precision_score(Test["Y"], Test["Y_predicted"]))
print("AUC:", scm.roc_auc_score(Test["Y"], Test["Y_predicted"]))