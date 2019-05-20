import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import SGDClassifier
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix
from sklearn.base import TransformerMixin, BaseEstimator
from pyvi import ViTokenizer, ViPosTagger

import re
import os
import json
import _pickle as cPickle # to save and load model

BASE_DIR = os.getcwd()


def get_test_data():
    filepath = BASE_DIR + '/raw_data/test_data.json'
    with open(filepath, 'r') as f:
        return json.load(f)

def get_train_data(n):
    filepath = BASE_DIR + '/raw_data/train_data.json'
    data = []
    with open(filepath, 'r') as f:
        bf = json.load(f)
        for d in bf[:n]:
            data.append(d)

    return data

# save the model
def savemodel(sgd):
    with open(BASE_DIR + "/model/classifier_model.pkl", "wb") as f:
        cPickle.dump(sgd, f)

# load the model
def loadmodel():
    with open(BASE_DIR + "/model/classifier_model.pkl", "rb") as f:
        return cPickle.load(f)
    return False

def train():
    # get 10000 record from dataset
    train_data = get_train_data(10000)
    # init data frame
    df_train = pd.DataFrame(train_data)

    # extract contents and tags from data frame
    contents = df_train['content'].values
    tags = df_train['category'].values

    # init training data and data test data
    contents_train, contents_test, tags_train, tags_test = train_test_split(
         contents, tags, test_size=0.25, random_state=1000
    )

    # init training engine - support vector machine
    sgd = Pipeline([
        ('vect', CountVectorizer()),
        ('tfidf', TfidfTransformer()),
        ('clf', SGDClassifier(loss='hinge', penalty='l2',alpha=1e-3, random_state=42, max_iter=5, tol=None)),
    ])

    # training...
    sgd.fit(contents_train, tags_train)
    
    savemodel(sgd)

def main():
    train()



if __name__ == "__main__":
    main()
