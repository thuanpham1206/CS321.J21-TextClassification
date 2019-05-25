from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import SGDClassifier
from sklearn.pipeline import Pipeline
from sklearn.metrics import (
    classification_report, accuracy_score, confusion_matrix,
    precision_recall_fscore_support
    )
import pandas as pd
import re
import os
import json
import _pickle as cPickle # for save and load model

BASE_DIR = os.getcwd()
MODEL_DIR = "model/classifier_model.pkl"

def get_test_data():
    filepath = BASE_DIR + '/datasource/test_data.json'
    with open(filepath, 'r') as f:
        return json.load(f)

def get_data():
    file_paths = [
        "datasource/json/train/train.json",
        "datasource/json/train/train1.json"
        ]

    data = []
    for path in file_paths:
        with open(os.path.join(BASE_DIR, path), 'r', encoding='utf-8') as f:
            bf = json.load(f)
            for d in bf:
                data.append(d)

    categories = set([x['category'] for x in data])

    return {
        "data": data,
        "categories": list(categories)
    }

# save the model
def savemodel(model):
    with open(os.path.join(BASE_DIR, MODEL_DIR), "wb") as f:
        cPickle.dump(model, f)

# load the model
def loadmodel():
    with open(os.path.join(BASE_DIR, MODEL_DIR), "rb") as f:
        return cPickle.load(f)
    return False

def get_categories():
    with open(os.path.join(BASE_DIR,
        "datasource/json/cache/categories.json"), 'r') as f:
        return json.load(f)
    return False


def removed_stopwords(dataset):
    stopwords = []
    with open(os.path.join(BASE_DIR,
        'datasource/stopwords/stopwords.txt')) as f:
        stopwords = [x.strip() for x in f.readlines()]

    # using regular expression to remove stopwords
    stopwords = re.compile(r'\b(?:%s)\b' % '|'.join(stopwords))
    
    removed = []
    for data in dataset:
        data['content'] = stopwords.sub('', data['content'])
        removed.append(data)

    return removed



def train():
    # get all records from dataset
    data = get_data()
    train_data = removed_stopwords(data['data'])

    # save categories set
    with open(os.path.join(BASE_DIR,
        "datasource/json/cache/categories.json"), 'w') as f:
        json.dump(data['categories'], f)

    # init data frame
    df_train = pd.DataFrame(train_data)

    # extract contents and tags from data frame
    contents = df_train['content'].values
    tags = df_train['category'].values

    # init train data and test data
    # contents and tags are train data
    # test_size=0.25 mean 25% size of the data has to be split as the test dataset
    # TODO: Not in use
    # reference: https://medium.com/@contactsunny/how-to-split-your-dataset-to-train-and-test-datasets-using-scikit-learn-e7cf6eb5e0d
    # contents_train, contents_test, tags_train, tags_test = train_test_split(
    #      contents, tags, test_size=0.1, random_state=42
    # )

    # init training engine - using support vector machine
    # use Pipleline to sticking multiple processes into a single scikit-learn estimator
    # sgd stand for stochastic gradient descent
    # reference: https://machinelearningcoban.com/2017/01/16/gradientdescent2/#-stochastic-gradient-descent
    # Just understand ideas and concepts
    sgd = Pipeline([
        # For feature extraction
        ('vect', CountVectorizer()),
        ('tfidf', TfidfTransformer()),
        # SGDClassifier is a Linear classifiers (SVM, logistic regression, a.o.) with SGD training.
        # params:
        # loss='hinge': (soft-margin) linear Support Vector Machine
        # panalty='l2' is the standard regularizer for linear SVM models
        # random_state=42: to make the results be the same when re-train
        ('clf', SGDClassifier(loss='hinge', penalty='l2',alpha=1e-3, random_state=42, max_iter=5)),
    ])

    # put train dataset into sgd
    sgd.fit(contents, tags)

    # TODO: add precision, recall and fscore, wait for test data
    # prediction = sgd.predict(contents_test)
    # score = precision_recall_fscore_support(prediction, tags_test)
    # print(score)
    savemodel(sgd)

def main():
    train()

if __name__ == "__main__":
    main()
