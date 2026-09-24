from Lab2 import *
def printer(message):
    print(str(message))


if __name__ == '__main__':
    d = 0x74D806F9F3A62BAE331FFE3F0A68AFE35B3D2E4794148AACBC26AA381CD7D30D
    n = 0xDCBFFE3E51F62E09CE7032E2677A78946A849DC4CDDE3A4D0CB81629242FB1A5
    e = 0x010001
    message1 = b'print(Hello, World!)'
    message2 = b'print(Goodbye, World!)'
    privateKey = (d, n)
    publicKey = (e, n)
    with open('Task4/out1.bin', 'rb') as f:
        M = f.read()
    with open('Task4/out2.bin', 'rb') as f:
        N = f.read()
