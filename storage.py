import os
from encryption import encrypt_text, decrypt_text

FILE ="diary.enc"

def file_exists():
    return os.path.exists(FILE)

def load_diary(password):
    """Read and decrypt diary"""
    if not file_exists():
        return "" # returns "" if there is no file yet.
    with open(FILE,"rb") as f:
        data = f.read()
    return decrypt_text(data,password)

def save_diary(text, password):
    """save it to the file and encrypt diary"""
    with open(FILE,"wb") as f:
        f.write(encrypt_text(text,password))



