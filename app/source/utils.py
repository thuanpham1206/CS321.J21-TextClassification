import pandas as pd
import os
import matplotlib.pyplot as plt
import json
import numpy as np
from sklearn.metrics import (
    precision_recall_fscore_support,
    precision_recall_curve,
    average_precision_score
    )
from train_md import BASE_DIR, CACHE_DIR
from train_md import loadmodel, removed_stopwords


def get_test_data():
    file_paths = [
        "app/storage/json/test/test.json",
        "app/storage/json/test/test1.json"
        ]

    data = []
    for path in file_paths:
        with open(os.path.join(BASE_DIR, path), 'r', encoding='utf-8') as f:
            bf = json.load(f)
            data = [x for x in bf]

    with open(os.path.join(BASE_DIR, CACHE_DIR, "testsize.json"), 'w') as f:
        json.dump({"size": len(data)}, f)

    return data


def predict(content):
    model = loadmodel()
    if not model:
        print("Model does'nt exist!")
        return False

    return model.predict([content])


def save(file, obj):
    with open(os.path.join(BASE_DIR, CACHE_DIR,
            file),'w') as f:
        for o in obj:
            f.write(o + "\n")

def _proba():
    model = loadmodel()
    test_data = removed_stopwords(get_test_data())
    df_test = pd.DataFrame(test_data)
    contents_test = df_test['content'].values
    tags_test = df_test['category'].values
    unique, counts = np.unique(tags_test, return_counts=True)
    print(dict(zip(unique, counts)))
    prediction = model.predict(contents_test)

    count = 0
    trues = []
    wrongs = []
    for i in range(451):
        if tags_test[i] != prediction[i]:
            count += 1
            trues.append(tags_test[i])
            wrongs.append(prediction[i])

    unique, counts = np.unique(np.array(trues), return_counts=True)
    print(dict(zip(unique, counts)))
    # print(wrongs)
    save('test_true.txt', tags_test)
    save('test_rs_1.txt', prediction)
    return {
        "all": precision_recall_fscore_support(prediction,tags_test,
        average=None),
        "avg": precision_recall_fscore_support(prediction,tags_test,
        average="micro")
    }

def chart():
    """
    Using precision-recall curve to evaluate the model
    Memo: https://machinelearningcoban.com/2017/08/31/evaluation/ 
    """
    def categories():
        with open(os.path.join(BASE_DIR, CACHE_DIR,
            "categories.json"), 'r') as f:
            return json.load(f)

    categories = categories()
    proba = _proba()
    precision, recall, fscore, sp = proba['all']
    plt.xlabel('recall')
    plt.ylabel('precision')
    plt.title('PR chart')
    plt.plot(sorted(recall, reverse=True),
            sorted(precision))
    plt.savefig(os.path.join(BASE_DIR, 'app/source/static/images/PRchart.png'))

    # close figur
    # cache proba
    with open(os.path.join(BASE_DIR, CACHE_DIR,
        "proba.json"), 'w') as f:
            pbavg = proba['avg']
            print(pbavg)
            json.dump({
                "precision": pbavg[0],
                "recall": pbavg[1],
                "fscore": pbavg[2],
            }, f, indent=4)
    
    return
    
def get_file_content(filepath):
    with open(filepath, 'r') as f:
        return f.read()
    return False

def common_info():
    res = {}
    with open(os.path.join(BASE_DIR, CACHE_DIR,
        "categories.json"), 'r') as f:
        res['categories'] = json.load(f)

    with open(os.path.join(BASE_DIR, CACHE_DIR,
        "testsize.json"), 'r') as f:
        res['testsize'] = json.load(f)['size']

    with open(os.path.join(BASE_DIR, CACHE_DIR,
        "trainsize.json"), 'r') as f:
        res['trainsize'] = json.load(f)['size']
    
    with open(os.path.join(BASE_DIR, CACHE_DIR,
        "proba.json"), 'r') as f:
            data = json.load(f)
            res.update({
                "precision": data['precision'],
                "recall": data['recall'],
                "fscore": data['fscore']
            })

    return res


if __name__ == "__main__":
    chart()

    