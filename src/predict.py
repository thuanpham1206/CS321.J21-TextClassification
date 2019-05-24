from train_md import loadmodel
# import pandas as pd


def predict(content):
    model = loadmodel()
    if not model:
        print("Model does'nt exist!")
        return False

    # Use for analytics, adding after
    # dataframe = pd.DataFrame({
    #     "content": content,
    #     "category": ""
    # })

    return model.predict([content])


def get_file_content(filepath):
    with open(filepath, 'r') as f:
        return f.read()
    return False




    