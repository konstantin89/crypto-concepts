# Signatures

Encryption and signature are two different systems.   
In some ways, they work in opposite directions.  

`With public-key encryption`, anybody can encrypt data with the public key.  
Only the owner of the private key can decrypt encrypted messages to recover the data.  

`With signatures`, only the owner of the private key can sign messages. 
Anybody can use the public key to verify the signature of a message.

## Generating key pairs commands
``` bash
# Generate private key
openssl genpkey -algorithm RSA -out private_key.pem -aes256

# Generate public key
openssl rsa -pubout -in private_key.pem -out public_key.pem
```
