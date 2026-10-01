from Lab2 import *
if __name__ == '__main__':
    n = 0xDCBFFE3E51F62E09CE7032E2677A78946A849DC4CDDE3A4D0CB81629242FB1A5
    e = 0x010001
    M = "A top secret!"
    d = 0x74D806F9F3A62BAE331FFE3F0A68AFE35B3D2E4794148AACBC26AA381CD7D30D
    m = M.encode().hex()
    m = int.from_bytes(m.encode(), 'big')
    publicKey = [e,n]
    cipherText = rsa_encrypt(m, publicKey)
    privateKey = [d, n]
    text = rsa_decrypt(cipherText, privateKey)
    print(f"{m}: {text}")