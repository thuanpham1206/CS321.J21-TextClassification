# manage

import sys
import os

argv = sys.argv

name = argv[0]
command = argv[1]

def run_command(path):
    pythoncommand = "python3 " if sys.version_info[0] < 3 else "python "
    os.system(pythoncommand + path)


def main():
    if command in ["train", "predict", "server"]:
        if command == "train":
            run_command("src/train_md.py")
            
        elif command == "predict":
            run_command("src/predict.py")

<<<<<<< HEAD
        else:
            run_command("src/index.py")
        
        return "\n" + command

    return "command '" + command + "' not found!"


print(main())
=======
if command == "server":
    run_command("src/index.py")
>>>>>>> 51caf4ad0a44033e09c5fc471777f516068b8fd3
