import os

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