import hashlib
import os

def get_file_hash(file_path):
    with open(file_path, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()

def check_integrity(file_path, expected_hash):
    current_hash = get_file_hash(file_path)
    if current_hash == expected_hash:
        print("File is intact")
    else:
        print("File has been modified")

file_path = 'example.txt'
# in the real app, original hash would be stored from previous run
original_hash = get_file_hash(file_path)
check_integrity(file_path, original_hash)