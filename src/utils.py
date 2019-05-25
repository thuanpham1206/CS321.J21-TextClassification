import pandas as pd
import os
import matplotlib.pyplot as plt
import json
from sklearn.metrics import precision_recall_fscore_support
from train_md import BASE_DIR, CACHE_DIR
from train_md import loadmodel

def get_test_data():
    file_paths = [
        "datasource/json/test/test.json",
        "datasource/json/test/test1.json"
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


def getscores():
    model = loadmodel()

    test_data = get_test_data()
    df_test = pd.DataFrame(test_data)
    contents_test = df_test['content'].values
    tags_test = df_test['category'].values
    # TODO: add precision, recall and fscore, wait for test data
    prediction = model.predict(contents_test)
    score = precision_recall_fscore_support(prediction, tags_test)
    return score


def plot_chart():
    """
    https://www.quora.com/What-is-Precision-Recall-PR-curve
    """
    precision, recall, fscore, support = getscores()
    plt.xlabel('recall')
    plt.ylabel('precision')
    plt.title('PR chart')
    plt.plot(sorted(recall.tolist(),reverse=True),
        sorted(precision.tolist()),
        marker=".")

    plt.savefig(os.path.join(BASE_DIR, 'src/static/images/PRchart.png'))

def chart_path():
    return os.path.join(BASE_DIR, 'src/static/images/PRchart.png') or False


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
    
    return res


if __name__ == "__main__":
    plot_chart()

    