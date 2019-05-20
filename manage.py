# manage

import sys
import os

argv = sys.argv

name = argv[0]
command = argv[1]

if command == "train":
    os.system("python src/train_md.py")

if command == "predict":
    os.system("python src/predict.py")