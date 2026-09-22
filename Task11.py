from Lab2 import *
if __name__ == '__main__':
    p = 0xF7E75FDC469067FFDC4E847C51F452DF
    q = 0xE85CED54AF57E53E092113E62F436F4F
    e = 0x0D88C3

    publicKey, privateKey = generate_rsa_key(p,q,e)
    print(f"The public key is: ({hex(publicKey[0])},{hex(publicKey[1])})")
    print(f"The private key is: {hex(privateKey)}")