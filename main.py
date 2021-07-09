import pathlib
from check_file import check_file_format


def create_summaries(path_to_this_dir):
    check_file_format(path_to_this_dir)

if __name__ == '__main__':
    create_summaries(pathlib.Path().resolve())