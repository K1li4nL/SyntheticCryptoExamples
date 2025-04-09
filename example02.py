from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import os

def main():
# Generate a random 256-bit (32 bytes) key and 128-bit (16 bytes) IV
    key = os.urandom(32)
    iv = os.urandom(16)

# Create the cipher object
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())

# Example message to encrypt
    message = b"Secret message"
# Pad the message to make its length a multiple of the block size
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(message) + padder.finalize()

# Encrypt the message
    encryptor = cipher.encryptor()
    encrypted_message = encryptor.update(padded_data) + encryptor.finalize()

    print("Encrypted message:", encrypted_message)

# Decrypt the message
    decryptor = cipher.decryptor()
    decrypted_padded_message = decryptor.update(encrypted_message) + decryptor.finalize()

# Unpad the decrypted message
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    decrypted_message = unpadder.update(decrypted_padded_message) + unpadder.finalize()

    print("Decrypted message:", decrypted_message.decode())

if __name__ == "__main__":
    main()
