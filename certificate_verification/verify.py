from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding

def load_certificate(file_path):
    with open(file_path, 'rb') as file:
        return x509.load_pem_x509_certificate(file.read(), default_backend())

def verify_certificate_chain(root_cert, intermediate_cert, server_cert):
    # Verify the server certificate against the Intermediate CA
    try:
        intermediate_cert.public_key().verify(
            server_cert.signature,
            server_cert.tbs_certificate_bytes,
            padding.PKCS1v15(),
            server_cert.signature_hash_algorithm
        )
    except Exception as e:
        print(f"Server certificate verification failed: {e}")
        return False

    # Verify the Intermediate CA certificate against the Root CA
    try:
        root_cert.public_key().verify(
            intermediate_cert.signature,
            intermediate_cert.tbs_certificate_bytes,
            padding.PKCS1v15(),
            intermediate_cert.signature_hash_algorithm
        )
    except Exception as e:
        print(f"Intermediate CA certificate verification failed: {e}")
        return False

    print("Certificate chain is valid.")
    return True

# Load certificates
root_cert = load_certificate('rootCA.crt')
intermediate_cert = load_certificate('intermediateCA.crt')
server_cert = load_certificate('server.crt')

# Verify the certificate chain
verify_certificate_chain(root_cert, intermediate_cert, server_cert)