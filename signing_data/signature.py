from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization

def load_private_key(file_path, passphrase):
    with open(file_path, "rb") as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=passphrase.encode(),  # Passphrase as bytes
            backend=None
        )
    return private_key

def load_public_key(file_path):
    with open(file_path, "rb") as key_file:
        public_key = serialization.load_pem_public_key(
            key_file.read(),
            backend=None
        )
    return public_key

def sign_data(private_key, data):

    print("[ ] Using private key to generate signature")

    signature = private_key.sign(
        data,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )

    print("[V] Generated signature", len(signature), " bytes long")

    return signature

def verify_signature(public_key, data, signature):

    print("[ ] Using public key to validate signature")

    try:
        public_key.verify(
            signature,
            data,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        print("[V] Signature is valid.")
    except Exception as e:
        print("[X] Signature verification failed:", e)

# params
private_key_path = "private_key.pem"
public_key_path = "public_key.pem"
file_to_sign = "data.txt"
private_key_pass = "root"

private_key = load_private_key(private_key_path, private_key_pass)
public_key = load_public_key(public_key_path)

# Read the file content
with open(file_to_sign, "rb") as file:
    data_to_sign = file.read()

# Sign the data with the private key
signature = sign_data(private_key, data_to_sign)

# Verify the signature with the public key
verify_signature(public_key, data_to_sign, signature)
