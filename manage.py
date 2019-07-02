# manage

import sys
import os
from subprocess import run, check_output
argv = sys.argv

name = argv[0]
command = argv[1]

VALID_CMD = ["train", "evaluate","server"]


def run_command(command):
    cmd_list = command.split(" ")
    out = str(check_output(["python3", "-V"]))
    if out and int(out[9]) == 3:
        run(["python3"] + cmd_list)
        return
    
    run(["python"] + cmd_list)

def recommend(wrong_cmd):
    for cmd in VALID_CMD:
        cmd_list = [x for x in cmd]
        wcmd_list = [x for x in wrong_cmd]
        if len([x for x in cmd_list if x in wcmd_list]) > 3:
            return ("'%s' not found! Do you mean '%s'" %(wrong_cmd, cmd))
    
    return (wrong_cmd + " not found!\n try: 'train', 'evaluate', 'server'")

def main():
    if command in VALID_CMD:
        if command == "train":
            run_command("app/source/train_md.py")

        elif command == "evaluate":
            run_command("app/source/utils.py")

        else:
            run_command("app/source/index.py")
        
        return "\nExit."

    return recommend(command)


print(main())