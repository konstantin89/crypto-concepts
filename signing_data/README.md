


## Generate a Root Certificate Authority (CA) Key and Self-Signed Certificate

``` bash
# Generate a Root CA private key
openssl genpkey -algorithm RSA -out rootCA.key -aes256

# Generate a self-signed Root CA certificate
openssl req -x509 -new -key rootCA.key -out rootCA.crt
```

