# CS321.J21-TextClassification
Yêu cầu nhóm: 
- Cài đặt pyvi và libsvm
- Upload các dataset vào thư mực data
Trang web để tải libsvm: https://www.csie.ntu.edu.tw/~cjlin/libsvm/#download
Cài đặt thư viện sk learn: https://scikit-learn.org/stable/install.html


# Update:
- Tạm thời train được các categories: "Life", "Business", "IT", "Science" từ 1000 records trong file raw_data/train_data.json
- File test data : raw_data/test_data.json
- Các bạn pull code về  chạy thử 
- Cài đặt các tất package (nếu cần) bằng lệnh:
    pip install -r requirements.txt
- Sau đó chạy file src/train_md.py:
    python train_md.py