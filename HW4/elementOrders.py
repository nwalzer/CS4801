import math

orders = [2, 3, 6, 7, 14, 21, 42]

resultDict = {}

for ord in orders:
    resultDict[ord] = []

for i in range(2, 43):
    for ord in orders:
        if pow(i, ord, 43) is 1:
            resultDict[ord].append(i)
            break

print(resultDict)