from json import (load as jsonload, dump as jsondump, loads as jsonloads)
from os import path


def save_data(json_file, data_file_path):
    with open(data_file_path, 'w') as f:
        f.write(json_file)


def load_data(data_file_path):
    try:
        with open(data_file_path, 'r') as f:
                data = jsonload(f)
        return data
    except Exception as ex:
        print(f'File error: {ex}')
        return []
    
    
