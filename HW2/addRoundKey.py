import mixColumns as MC

def main():
    key = "0 0 1 1 0 1 0 0 0 0 0 0 1 0 0 1 1 0 1 0 0 1 1 0 1 1 0 1 0 1 1 0 0 1 1 1 0 1 1 0 1 0 0 1 0 0 1 1 0 0 1 0 1 0 0 0 0 1 0 0 0 0 1 1 1 1 0 1 0 1 0 1 0 0 0 0 0 1 0 0 1 1 0 0 1 0 0 0 1 1 0 0 1 1 0 1 1 1 1 1 0 0 0 1 1 0 1 1 0 1 0 1 0 1 1 1 0 0 1 0 0 1 1 1 0 0 1 0".replace(" ", "")
    vals = MC.discrete()
    output = []

    for i in range(16):
        val = int(vals[i], 16)
        keyString = ""
        for j in range(8):
            keyString += key[i*8 + j]
        toXor = int(keyString, 2)
        output.append(hex(val ^ toXor))
    print("-------------")
    MC.printResult(output)

if __name__ == '__main__':
    main()