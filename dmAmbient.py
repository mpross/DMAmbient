import os
import re

import nltk
import pandas as pd
import numpy as np

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.neural_network import MLPClassifier

stopword = nltk.corpus.stopwords.words('english')
wn= nltk.WordNetLemmatizer()


def tokenize(text):

    tokens = re.split('\W+',text)
    return tokens


def remove_stopwords(tokenezed_list):

    text = [word for word in tokenezed_list if word not in stopword]
    return text


def lemmatizing(tokenized_text):
    text = [wn.lemmatize(word) for word in tokenized_text]
    return text


def onehot(label):
    if label == 'tavern':
        return np.array([1, 0, 0, 0])
    if label == 'town':
        return np.array([0, 1, 0, 0])
    if label == 'dung':
        return np.array([0, 0, 1, 0])
    if label == 'none':
        return np.array([0, 0, 0, 1])


directory = 'corpus/tagged/'

fileIndex = 0

for filename in os.listdir(directory):

    rawData = open(directory + filename).read()

    data = pd.read_csv(directory + filename, sep='\t',names=['label', 'body_text'],header=None)

    data['body_text_tokenized'] = data['body_text'].apply(lambda x: tokenize(x))

    data['body_text_nostop'] = data['body_text_tokenized'].apply(lambda x: remove_stopwords(x))

    data['body_text_lemmatized'] = data['body_text_nostop'].apply(lambda x: lemmatizing(x))

    count_vect = CountVectorizer()
    X_counts = count_vect.fit_transform(data['body_text'])
    print(X_counts.shape)

    data['tag'] = data['label'].apply(lambda x: onehot(x))

    print(np.array(data['tag'].values).astype('int'))

    net = MLPClassifier(solver='lbfgs', alpha =1e-5, hidden_layer_sizes=(5, 2), random_state=1)
    x = X_counts
    y = data['tag'].values.astype('int')
    net.fit(x, y)
    net.predict(X_counts[1])

    fileIndex += 1

    if fileIndex>=2:
        break