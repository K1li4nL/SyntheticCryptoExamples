from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
import os

# Party 1 (Alice) generates private and public keys for ECDH
alice_private_key = ec.generate_private_key(ec.SECP384R1(), default_backend())
alice_public_key = alice_private_key.public_key()

# Party 2 (Bob) generates private and public keys for ECDH
bob_private_key = ec.generate_private_key(ec.SECP384R1(), default_backend())
bob_public_key = bob_private_key.public_key()

# Alice and Bob exchange public keys (this would typically happen over an insecure channel)
# Alice uses Bob's public key to perform the shared key computation
alice_shared_key = alice_private_key.exchange(ec.ECDH(), bob_public_key)

# Bob uses Alice's public key to compute the shared key
bob_shared_key = bob_private_key.exchange(ec.ECDH(), alice_public_key)

# Both Alice and Bob should now have the same shared secret, but an eavesdropper cannot calculate it
assert alice_shared_key == bob_shared_key  # This will always be True

print("Shared secret computed by both Alice and Bob:", alice_shared_key.hex())

# Derive a symmetric key from the shared secret using PBKDF2
# (this is often done to generate a key for AES or other symmetric ciphers)
salt = os.urandom(16)  # Random salt for key derivation
iterations = 100000

kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,  # 256-bit key for AES
    salt=salt,
    iterations=iterations,
    backend=default_backend()
)

symmetric_key = kdf.derive(alice_shared_key)  # Use Alice's shared secret to derive the symmetric key

print("Derived symmetric key (for AES or other ciphers):", symmetric_key.hex())
