from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

# Generate an elliptic curve private key
private_key = ec.generate_private_key(ec.SECP384R1(), default_backend())

# Get the corresponding public key
public_key = private_key.public_key()

# Message to be signed
message = b"Cryptography with elliptic curves"

# Sign the message with the private key
signature = private_key.sign(
    message,
    ec.ECDSA(hashes.SHA256())
)

# Verify the signature using the public key
try:
    public_key.verify(
        signature,
        message,
        ec.ECDSA(hashes.SHA256())
    )
    print("Signature is valid.")
except Exception as e:
    print(f"Signature verification failed: {e}")

# Optionally, serialize the private and public keys (for use in storage or sharing)
private_pem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
)

public_pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

# Print the serialized private and public keys
print("Private key:", private_pem.decode())
print("Public key:", public_pem.decode())

