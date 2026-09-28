from Lab2 import *

if __name__ == '__main__':
    d = 0x74D806F9F3A62BAE331FFE3F0A68AFE35B3D2E4794148AACBC26AA381CD7D30D
    n = 0xDCBFFE3E51F62E09CE7032E2677A78946A849DC4CDDE3A4D0CB81629242FB1A5
    e = 0x010001
    privateKey = (d, n)
    publicKey = (e, n)
    with open('Task4/a1.out', 'rb') as f: # Benign Program
        M = f.read()
    with open('Task4/a2.out', 'rb') as f: # Malicious program
        N = f.read()
    hash1 = hashlib.md5(M).hexdigest()
    hash2 = hashlib.md5(N).hexdigest()
    sign1 = sign_md5_hash(hash1, privateKey)
    sign2 = sign_md5_hash(hash2, privateKey)

    print(f"Signature of benign program: {hex(sign1)}")
    print(f"Signature of evil program: {hex(sign2)}")

    if verify_md5_hash(hash1,sign1, publicKey) & verify_md5_hash(hash1,sign2, publicKey):
        print(f'The signatures are equal and correct')