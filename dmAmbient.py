import os
import re

import nltk
import pandas as pd

from sklearn.feature_extraction.text import CountVectorizer

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
    print(count_vect.get_feature_names())

    fileIndex += 1

    if fileIndex>=2:
        break