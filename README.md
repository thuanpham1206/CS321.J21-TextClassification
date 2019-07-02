# Runtime:
    Python's version >= 3.5.2

# Update - guideline:
1. clone/pull code from repository:
    - git clone https://github.com/thuanpham1206/CS321.J21-TextClassification
    - git pull

2. Install package dependencies (if any)
    - pip install -r requirements.txt

3. how to?
    - Make sure you are in the root folder of project
    - run the following command: python manage.py {argument}
    - supported arguments:
        + train: training the model
        + evaluate: generate precision-recall chart and save it.
        + server: run server
    - example:
        + python manage.py server
        + or python3 manage.py server
