import os

def check_file_format(path):
    
    list_of_valid_filenames = []
    
    for filename in os.listdir(path):
        if filename.endswith(".fit") or filename.endswith(".gpx"): 
            list_of_valid_filenames.append(os.path.join(path,filename))
        else:
            continue
    
    return list_of_valid_filenames