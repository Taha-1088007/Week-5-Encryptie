import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

SALT_LENGTH = 16
ITERATIONS = 600_000


def make_key(password, salt):
    """make a password from a key"""

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=ITERATIONS,
    )
    return base64.urlsafe_b64encode(kdf.derive(password.encode()))


def encrypt_text(text, password):
    salt = os.urandom(SALT_LENGTH) # new random salt every time
    key = make_key(password, salt)
    encrypted = Fernet(key).encrypt(text.encode())
    return salt + encrypted

def decrypt_text(data, password):
    salt =data[:SALT_LENGTH] #the first 16 bytes are the salt
    encrypted = data[SALT_LENGTH:]
    key = make_key(password, salt)
    return Fernet(key).decrypt(encrypted).decode()