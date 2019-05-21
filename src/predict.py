from train_md import loadmodel
# import pandas as pd


def predict(content):
    model = loadmodel()
    if not model:
        print("Model does'nt exist!")
        return False

    # Use for analytics
    # dataframe = pd.DataFrame({
    #     "content": content,
    #     # "category": "Bussi"
    # })

    return model.predict([content])


def get_file_content(filepath):
    with open(filepath, 'r') as f:
        return f.read()
    return False


def main():
    filepath = "test1.txt"
    res = (predict(
        get_file_content(filepath)
    ))

    print("predicted results for :", filepath)
    for r in res:
        print(r)

if __name__ == "__main__":
    main()




    