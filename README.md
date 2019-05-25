# CS321.J21-TextClassification
Yêu cầu nhóm: 
- Cài đặt pyvi và libsvm
- Upload các dataset vào thư mực data

# Update - guideline:
1. clone/pull code from repository:
    - git clone https://github.com/thuanpham1206/CS321.J21-TextClassification
    - git pull

2. Install package dependencies (if any)
    - pip install -r requirements.txt

3. how to run?
    - Make sure you are in the root folder of project
    - run the following command: python manage.py {argument}
    - supported arguments:
        + train: training the model
        + evl: generate precision-recall chart and save it.
        + server: run server
    - example:
        + python manage.py server

# Đánh giá độ chính xác, độ bao phủ, f scores
Viết thêm một đoạn code để tính score
