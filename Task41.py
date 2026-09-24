if __name__ == '__main__':
    with open('Task4/out1.bin', 'rb') as f:
        out1 = f.read()
    with open('Task4/out2.bin', 'rb') as f:
        out2 = f.read()
    out1 = int.from_bytes(out1, 'big')
    out2 = int.from_bytes(out2, 'big')
    xord = out1 ^ out2
    xord = hex(xord)
    print(xord)