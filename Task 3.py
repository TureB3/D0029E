from Lab2 import *
from Task3.Modulus1 import Modulus1 as n
from Task3.Signature import signature
import hashlib
def verify_hash(h, s, public_key):
    e,n = public_key
    s = power(s, e, n)
    s = s.to_bytes((s.bit_length() + 7)//8, "big") # Converts the padded decrypted message to the correct bytes
    s=s[-32:] # To remove the salt added by the PSS padding scheme
    print(s.hex())
    print(h)
    return h == s.hex()


if __name__ == '__main__':
    # Website: saab.se
    # Uses SHA256 digest with RSA-PSS signature
    e = 65537
    publicKey1 = (e,n)
    with open("Task3/c0_body.bin", 'rb') as f:
        data = f.read()
    hash1 = hashlib.sha256(data).hexdigest()



    if verify_hash(hash1, signature, publicKey1):
        print('It Worked')
    else:
        print('It Not Work')

