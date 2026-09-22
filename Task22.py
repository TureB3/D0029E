from Lab2 import *
if __name__ == '__main__':
    M = "Launch a missile."
    S = 0x643D6F34902D9C7EC90CB0B2BCA36C47FA37165C0005CAB026C0542CBDB6802F
    e = 0x010001
    n = 0xAE1CD4DC432798D933779FBD46C6E1247F0CF1233595113AA51B450F18116115

    publicKey = (e,n)
    plaintext = rsa_decrypt(S, publicKey)
    print(f"Alice's message: {plaintext}")