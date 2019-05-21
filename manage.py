# manage

import sys
import os

argv = sys.argv

name = argv[0]
command = argv[1]

def run_command(path):
    pythoncommand = "python3 " if sys.version_info[0] < 3 else "python3 "
    os.system(pythoncommand + path)

if command == "train":
    run_command("src/train_md.py")

if command == "predict":
    run_command("src/predict.py")

if command == "server":
    run_command("src/index.py")