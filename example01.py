import hashlib
import os

# Simple hash function
def hash_file(file_path):
    sha256 = hashlib.sha256()
    with open(file_path, 'rb') as f:
        while chunk := f.read(8192):
            sha256.update(chunk)
    return sha256.hexdigest()

# Encrypt and decrypt example with Fernet (Cryptography library)
from cryptography.fernet import Fernet

def encrypt_decrypt_example():
    key = Fernet.generate_key()
    cipher = Fernet(key)
    message = "This is a secret message"
    encrypted_message = cipher.encrypt(message.encode())
    decrypted_message = cipher.decrypt(encrypted_message)
    return decrypted_message.decode()

# Simple usage (testing)
if __name__ == "__main__":
    file_hash = hash_file("example_file.txt")  # Make sure this file exists
    decrypted_message = encrypt_decrypt_example()
    print(f"File Hash: {file_hash}")
    print(f"Decrypted Message: {decrypted_message}")

