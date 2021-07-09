import os
import sys

def check_file_format(path):
    for filename in os.listdir(path):
        if filename.endswith(".fit") or filename.endswith(".py"): 
            print(os.path.join(path, filename))
        else:
            continue