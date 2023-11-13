from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding

private_key_password = "root" 

# Load the existing private key from a file
with open("private_key.pem", "rb") as private_key_file:
    private_key = serialization.load_pem_private_key(
        private_key_file.read(),
        password=private_key_password.encode(),
        backend=default_backend()
    )

# Load the existing public key from a file
with open("public_key.pem", "rb") as public_key_file:
    public_key = serialization.load_pem_public_key(
        public_key_file.read(),
        backend=default_backend()
    )

# Encrypt a message with the public key
message = b"Hello, world!"
ciphertext = public_key.encrypt(
    message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# Decrypt the message with the private key
decrypted_message = private_key.decrypt(
    ciphertext,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

print("Original Message:", message.decode())
print("Decrypted Message:", decrypted_message.decode())

