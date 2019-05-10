import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
# from nltk.corpus import stopwords
from sklearn.model_selection import train_test_split
from sklearn.linear_model import SGDClassifier
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix


import re
import os
import json


BASE_DIR = os.getcwd().replace("src", "")
KEYS_2_TAG = {
    "1": "kinh doanh",
    "2": "thời sự",
    "3": "thế giới",
    "4": "thể thao",
    "5": "pháp luật",
    "6": "giáo dục",
    "7": "số hóa",
    "8": "ý kiến",
    "9": "sức khỏe",
    "10": "xe"
}
TAG_2_KEY = {
    "kinh doanh": "1",
    "thời sự": "2",
    "thế giới": "3",
    "thể thao": "4",
    "pháp luật": "5",
    "giáo dục": "6",
    "số hóa": "7",
    "ý kiến": "8",
    "sức khỏe": "9",
    "10": "xe"
}



stopwords = []

def cleaned_text(text):
    return text
    text = text.lower()
    text = " ".join(word for word in text.split() if word not in stopwords)
    # return re.sub(r"[^a-z ]", "", text)
    return text.replace("\n", "")


def get_data():
    data = []
    filepath = BASE_DIR + 'raw_data/vn_express_data/vn_express.txt'
    df = pd.read_csv(filepath, names=['text', 'tag'], sep='\t')
    data.append(df)
    return data



def main():
    data = get_data()
    df = pd.concat(data)
    # print(df)
    sentences = df['text'].values
    tags = df['tag'].values
    
    sentences_train, sentences_test, tags_train, tags_test = train_test_split(
         sentences, tags, test_size=0.25, random_state=1000
    )
    vectorizer = CountVectorizer(min_df=0, lowercase=False)
    vectorizer.fit(sentences_train)
    # print(vectorizer.transform(sentences_train))
    # print(vectorizer.transform(sentences_test))

    sgd = Pipeline([
        ('vect', CountVectorizer()),
        ('tfidf', TfidfTransformer()),
        ('clf', SGDClassifier(loss='hinge', penalty='l2',alpha=1e-3, random_state=42, max_iter=5, tol=None)),
    ])

    sgd.fit(sentences_train, tags_train)
    print(tags_train, tags_test)
    tag_prediction = sgd.predict(sentences_test)
    print('accuracy %s' % accuracy_score(tag_prediction, tags_test))

    # print(classification_report(tags_test, y_pred,target_names=tags))



if __name__ == "__main__":
    main()

# vectorizer = CountVectorizer(min_df=0, lowercase=False)
# sentences = ['John likes ice cream', 'John hates chocolate.']
# vectorizer.fit(sentences)
# # print(vectorizer.vocabulary_)
# print(vectorizer.transform(sentences).toarray())