import pathlib
from check_file import check_file_format
from create_summary import summarize


def create_summaries(path_to_this_dir):
    
    valid_files = check_file_format(path_to_this_dir)

    for activity, type in valid_files.items():
        summarize(activity, type)

if __name__ == '__main__':
    create_summaries(pathlib.Path().resolve())