import os
import shutil
import string
import time

def list_directory_contents(path):
    for item in os.listdir(path):
        if os.path.isdir(os.path.join(path, item)):
            print(item)
    for item in os.listdir(path):
        if os.path.isfile(os.path.join(path, item)):
            print(item)
    for item in os.listdir(path):
        print(item)

def check_access(path):
    return {
        'exists': os.path.exists(path),
        'readable': os.access(path, os.R_OK),
        'writable': os.access(path, os.W_OK),
        'executable': os.access(path, os.X_OK)
    }

def test_path(path):
    if os.path.exists(path):
        return {
            'filename': os.path.basename(path),
            'directory': os.path.dirname(path)
        }
    return 'Path does not exist'

def count_lines_in_file(file_path):
    with open(file_path, 'r') as file:
        return sum(1 for _ in file)

def write_list_to_file(file_path, data):
    with open(file_path, 'w') as file:
        for item in data:
            file.write(f'{item}\n')

def generate_text_files():
    for letter in string.ascii_uppercase:
        with open(f'{letter}.txt', 'w') as file:
            file.write(letter)

def copy_file(src, dest):
    shutil.copy(src, dest)

def delete_file(path):
    if os.path.exists(path) and os.access(path, os.W_OK):
        os.remove(path)
    else:
        print('File cannot be deleted')
