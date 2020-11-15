def discrete():
    initialValues = [[0xB1, 0x6D, 0x5E, 0x84], [0x1B, 0x72, 0x0D, 0x37], [0x0C, 0x97, 0xD4, 0x1A], [0x0B, 0x98, 0xB9, 0x80]] #each inner list is one column
    endingVals = []
    for i in range(4):
        vals = initialValues[i]

        val1 = mult2(vals[0]) ^ mult3(vals[1]) ^ vals[2] ^ vals[3]
        val2 = vals[0] ^ mult2(vals[1]) ^ mult3(vals[2]) ^ vals[3]
        val3 = vals[0] ^ vals[1] ^ mult2(vals[2]) ^ mult3(vals[3])
        val4 = mult3(vals[0]) ^ vals[1] ^ vals[2] ^ mult2(vals[3])
        endingVals.append(hex(val1 & 0xFF))
        endingVals.append(hex(val2 & 0xFF))
        endingVals.append(hex(val3 & 0xFF))
        endingVals.append(hex(val4 & 0xFF))
    printResult(endingVals)
        
def printResult(endingVals):
    for i in range(4): #print results as the exact matrix it should be
        toPrint = ""
        for k in range(4):
            toPrint += endingVals[i + 4*k] + "\t"
        print(toPrint)

def mult3(val):
    return val ^ mult2(val)

def mult2(val):
    newVal = val << 1
    if val & 0x80 is 0x80:
        newVal = newVal ^ 0x1B
    return newVal

discrete()