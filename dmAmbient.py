import nltk
import pandas as pd
import os
import re

stopword = nltk.corpus.stopwords.words('english')

def tokenize(text):

    tokens = re.split('\W+',text)
    return tokens

def remove_stopwords(tokenezed_list):

    text = [word for word in tokenezed_list if word not in stopword]
    return text

directory = 'corpus/tagged/'

fileIndex = 0

for filename in os.listdir(directory):

    rawData = open(directory + filename).read()

    data = pd.read_csv(directory + filename, sep='\t',names=['label', 'body_text'],header=None)

    data['body_text_tokenized'] = data['body_text'].apply(lambda x: tokenize(x))

    data['body_text_nostop'] = data['body_text_tokenized'].apply(lambda x: remove_stopwords(x))

    print(data.head())

    fileIndex += 1

    if fileIndex>=2:
        break