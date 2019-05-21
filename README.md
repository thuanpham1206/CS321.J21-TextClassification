# CS321.J21-TextClassification
Yêu cầu nhóm: 
- Cài đặt pyvi và libsvm
- Upload các dataset vào thư mực data
Trang web để tải libsvm: https://www.csie.ntu.edu.tw/~cjlin/libsvm/#download
Cài đặt thư viện sk learn: https://scikit-learn.org/stable/install.html


# Update - guideline:
1. clone/pull code from repository:
    - git clone https://github.com/thuanpham1206/CS321.J21-TextClassification
    - git pull

2. Install package dependencies
    - pip install -r requirements.txt

3. how to run?
    - Make sure you are in the root folder of project
    - run the following command: python manage.py {argument}
    - supported arguments:
        + train: training the model
        + predict: trying predict a test file
        + server: run server
    - example:
        + python manage.py predict

4. Edit test data in test1.txt (copy content from acticles of vnexpress, vietnamnet, ...)
