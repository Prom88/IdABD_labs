import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB


spamStats = pd.read_csv("з13/spam.csv", index_col="isSpam")

wordsStats = pd.read_csv("з13/words.csv")


spamChance = spamStats.at[1, 'Писем'] / spamStats.at[0, 'Писем']


X_train = np.array([wordsStats["спам"].values, wordsStats["не спам"].values])
y_train = np.array([1, 0])



model = MultinomialNB(alpha=0.2)
yu = model.fit(X_train, y_train)



def predictSpam(message):
    words_in_msg = message.lower().split()
    msg_vector = np.zeros(len(wordsStats))
    print(words_in_msg)

    for i, word in enumerate(wordsStats["word"]):
        msg_vector[i] = words_in_msg.count(word.lower())

    msg_vector = msg_vector.reshape(1, -1)
    print(msg_vector)
    prediction = model.predict(msg_vector)
    probabilities = model.predict_proba(msg_vector)[0]
    
    if prediction == 1:
        print("спам")
    else:
        print("не спам")


    print("F(не спам) и F(спам):",probabilities)


print("вероятность, что письмо является спамом:", round(spamChance, 3))



predictSpam("Access cash rEmOve Refund Million Investment Bonus")





