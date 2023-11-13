# Asymmetric key encryption

## Encrypt with public key, decrypt with private key
This is the important concept behind assimetric key encryption:  
`Every public key can encrypt data. Only the one private key can decrypt it.`  

Be careful! this is the opposite of signature mechanisms!   
In signatures, only the private key holder can sign, but every   
public key holder can validate signature.   

## Generating key pairs commands
``` bash
# Generate private key
openssl genpkey -algorithm RSA -out private_key.pem -aes256

# Generate public key
openssl rsa -pubout -in private_key.pem -out public_key.pem
```
