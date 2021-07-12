import pathlib
from create_summary import summarize
import os

# Find the .gpx and .fit files
def check_file_format(path):
    dict_of_valid_filenames = {}
    for filename in os.listdir(path):
        if filename.endswith(".fit"): 
            dict_of_valid_filenames[os.path.join(path,filename)] = ".fit"
        elif filename.endswith(".gpx"):
            dict_of_valid_filenames[os.path.join(path,filename)] = ".gpx"
        else:
            continue
    return dict_of_valid_filenames

# MAIN FUNCTION
def main(path_to_this_dir):
    valid_files = check_file_format(path_to_this_dir)
    for activity, type in valid_files.items():
        summarize(activity, type)

if __name__ == '__main__':
    main(pathlib.Path().resolve())