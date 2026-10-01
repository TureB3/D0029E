from Lab2 import *
if __name__ == '__main__':
    message = b'Launch a missile.'
    md5_hash = hashlib.md5(message).hexdigest()
    print(md5_hash)
    d = 0x74D806F9F3A62BAE331FFE3F0A68AFE35B3D2E4794148AACBC26AA381CD7D30D
    n = 0xDCBFFE3E51F62E09CE7032E2677A78946A849DC4CDDE3A4D0CB81629242FB1A5
    e = 0x010001
    privateKey = (d,n)
    publicKey = (e,n)
    sign = sign_md5_hash(md5_hash, privateKey)
    print(hex(sign)[2:])

    if verify_md5_hash(md5_hash, sign, publicKey):
        print('It Worked')
    else:
        print('It Not Work')