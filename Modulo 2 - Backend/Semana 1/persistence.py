from json import (load as jsonload, dump as jsondump, loads as jsonloads)
from os import path
from utilities import log_exception

def save_data(json_file, data_file_path):
    with open(data_file_path, 'w') as f:
        f.write(json_file)


def load_data(data_file_path):
    try:
        with open(data_file_path, 'r') as f:
                data = jsonload(f)
        return data
    except Exception as ex:
        log_exception(ex)
        return []
    
    
