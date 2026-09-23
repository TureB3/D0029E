# Function to find modular inverse of e modulo phi(n)
# Here we are calculating phi(n) using Hit and Trial Method
# but we can optimize it using Extended Euclidean Algorithm
from math import trunc
import hashlib
def sign_md5_hash(m, private_key):
    message = int.from_bytes(m.encode(), 'big')
    sign = power(message, private_key[0], private_key[1])
    return sign
def verify_md5_hash(m, s, public_key): # Task 2.4
    message = int.from_bytes(m.encode(), 'big')
    toverify = power(s, public_key[0], public_key[1])
    if message == toverify:
        return True
    else:
        return False
def modInverse(n, m):
    x = [0]
    y = [0]

    g = gcdExtended(n, m, x, y)
    if g != 1:
        return -1
    else:

        # m is added to handle negative x
        res = (x[0] % m + m) % m
        return res

# Function to calculate gcd
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Extended recursive gcd function to return the private key d as the input x[0]
def gcdExtended(a, b, x, y):

    # Base Case
    if a == 0:
        x[0] = 0
        y[0] = 1
        return b

    # To store results of recursive call
    # Fungerar genom 1 length array som aliasar inuti funktionen och uppdateras så att ax + by = 1 i alla steg
    # I slutändan kommer x[0] som skickas in från modInverse funktionen aliasas och returneras som private key
    x1 = [0]
    y1 = [0]
    gcd = gcdExtended(b % a, a, x1, y1)

    # Update x and y using results of recursive call
    x[0] = y1[0] - (b // a) * x1[0]
    y[0] = x1[0]

    return gcd

def generate_rsa_key(p,q,e):
    n = p * q
    phi = (p - 1) * (q - 1)


    # Compute d such that e * d ≡ 1 (mod phi(n))
    d = modInverse(e, phi)

    return (e,n), (d,n)


# Modular arithmetic exponentiation
def power(base, expo, m):
    res = 1
    base = base % m
    while expo > 0:
        if expo & 1:
            res = (res * base) % m
        base = (base * base) % m
        expo = expo // 2
    return res

# Encrypt message using public key (e, n), and return it as a hex value
def rsa_encrypt(m, publicKey):
    return power(m, publicKey[0], publicKey[1]) # Intentionally keeping them as numbers to be able to more easily decrypt

# Decrypt message using private key (d, n)
def rsa_decrypt(c, privatekey):
    plaintext = power(c, privatekey[0], privatekey[1])
    plaintext = hex(plaintext)[2:] #[2:] is there to remove the 0x used for formatting as hex
    return bytes.fromhex(plaintext).decode("utf-8")

if __name__ == '__main__':
    p = 0xF7E75FDC469067FFDC4E847C51F452DF
    q = 0xE85CED54AF57E53E092113E62F436F4F
    e = 0x0D88C3

    publicKey, privateKey = generate_rsa_key(p,q,e)
    print(f"The public key is: ({hex(publicKey[0])},{hex(publicKey[1])})")
    print(f"The private key is: {hex(privateKey[0])}")
