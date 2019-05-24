# manage

import sys
import os

argv = sys.argv

name = argv[0]
command = argv[1]

def run_command(path):
    pythoncommand = "python " if sys.version_info[0] < 3 else "python3 "
    os.system(pythoncommand + path)


def main():
    if command in ["train", "server"]:
        if command == "train":
            run_command("src/train_md.py")

        # not in use
        # elif command == "predict":
        #     run_command("src/predict.py")

        else:
            run_command("src/index.py")
        
        return "\nExit!"

    return "command '" + command + "' not found!"


print(main())
