from train_md import loadmodel
# import pandas as pd


def predict(content):
    model = loadmodel()
    if not model:
        print("Model does'nt exist!")
        return False

    return model.predict([content])


def evaluate(test_dateset):
    model = loadmodel()

    # Use for analytics, adding after
    dataframe = pd.DataFrame(test_dateset)

    return model.predict(dataframe)



def get_file_content(filepath):
    with open(filepath, 'r') as f:
        return f.read()
    return False




    