from Lab2 import *
if __name__ == '__main__':
    p = 0xF7E75FDC469067FFDC4E847C51F452DF
    q = 0xE85CED54AF57E53E092113E62F436F4F
    e = 0x0D88C3

    publicKey, privateKey = generate_rsa_key(p,q,e)
    M = "I owe you $2000"
    m = M.encode().hex()
    m = int.from_bytes(m.encode(), 'big')
    sign1 = rsa_encrypt(m, privateKey)
    print(f"Signature 1 for $2000: {sign1}")
    M2 = "I owe you $3000"
    m2 = M2.encode().hex()
    m2 = int.from_bytes(m2.encode(), 'big')
    sign2 = rsa_encrypt(m2, privateKey)
    print(f"Signature 2 for $3000: {sign2}")