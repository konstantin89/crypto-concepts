# Certificates verification

Here we have example of certificate chains verification.  
We use 3 certificates:  
Root CA -> Intermediate CA -> Server certificate

## Verify intermediate CA with root CA 

Here we generate Root CA and intermediate CA.  
Then we verify intermediate CA with root CA.

```bash 

# Step 1 - Generate a private key for the Root CA
openssl genpkey -algorithm RSA -out rootCA.key -aes256

# Generate a self-signed Root CA certificate
openssl req -x509 -new -key rootCA.key -out rootCA.crt


# Step 2 - Generate Intermediate CA:

# Generate a private key for the Intermediate CA
openssl genpkey -algorithm RSA -out intermediateCA.key -aes256

# Generate a Certificate Signing Request (CSR) for the Intermediate CA
openssl req -new -key intermediateCA.key -out intermediateCA.csr

# Sign the CSR with the Root CA to get the Intermediate CA certificate
openssl x509 -req -in intermediateCA.csr -CA rootCA.crt -CAkey rootCA.key -CAcreateserial -out intermediateCA.crt

# Step 3 - Verify Intermediate CA with Root CA:

# Verify the Intermediate CA certificate against the Root CA
openssl verify -CAfile rootCA.crt intermediateCA.crt
```

## Generate server certificate and verify against security chain

First, generate server certificate signed by intermediate CA:

``` bash 
# Generate a private key for the server
openssl genpkey -algorithm RSA -out server.key

# Generate a Certificate Signing Request (CSR) for the server
openssl req -new -key server.key -out server.csr

# Sign the CSR with the Intermediate CA to get the server certificate
openssl x509 -req -in server.csr -CA intermediateCA.crt -CAkey intermediateCA.key -CAcreateserial -out server.crt
```

Then use `verify.py` to verify the whole security chain:
rootCA.crt -> intermediateCA.crt -> server.crt