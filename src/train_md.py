import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import SGDClassifier
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix
from sklearn.base import TransformerMixin, BaseEstimator
# from pyvi import ViTokenizer, ViPosTagger


import re
import os
import json


BASE_DIR = os.getcwd().replace("src", "")


stopwords = []

def cleaned_text(text):
    return text
    text = text.lower()
    text = " ".join(word for word in text.split() if word not in stopwords)
    # return re.sub(r"[^a-z ]", "", text)
    return text.replace("\n", "")


def get_test_data():
    filepath = BASE_DIR + 'raw_data/test_data.json'
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def get_train_data(n):
    filepath = BASE_DIR + 'raw_data/train_data.json'
    data = []
    with open(filepath, 'r', encoding='utf-8') as f:
        bf = json.load(f)
        for d in bf[:n]:
            data.append(d)

    return data


def main():
    train_data = get_train_data(1000)
    df_train = pd.DataFrame(train_data)
    # print(df)
    sentences = df_train['content'].values
    tags = df_train['category'].values
    # print(tags)
    sentences_train, sentences_test, tags_train, tags_test = train_test_split(
         sentences, tags, test_size=0.25, random_state=1000
    )


    sgd = Pipeline([
        # ('transformer', FeatureTransformer()),
        ('vect', CountVectorizer()),
        ('tfidf', TfidfTransformer()),
        ('clf', SGDClassifier(loss='hinge', penalty='l2',alpha=1e-3, random_state=42, max_iter=5, tol=None)),
    ])

    sgd.fit(sentences_train, tags_train)

    test_data = get_test_data()
    df_test = pd.DataFrame(test_data)
    tag_prediction = sgd.predict(df_test['content'])
    print(tag_prediction)

    # print('accuracy %s' % accuracy_score(tag_prediction, tags_test))
    # print(len(tag_prediction), len(tags_test), len(tags))
    # print(classification_report(tags_test, tag_prediction,target_names=tags))



if __name__ == "__main__":
    main()
