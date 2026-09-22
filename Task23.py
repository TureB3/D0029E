from Lab2 import *
if __name__ == '__main__':
    message = b'Launch a missile.'
    md5_hash = hashlib.md5(message).hexdigest()
    print(md5_hash)