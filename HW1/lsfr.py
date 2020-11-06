# state = [0, 0, 1, 0, 1, 1, 0]
# gates = [1, 1, 0, 0, 0, 0, 1]
#
#       ----------<------------------<-------
#       |     |    |                        |
#       -> 0 -> 0 -> 1 -> 0 -> 1 -> 1 -> 0 -> output



state=[0, 0, 1, 0, 1, 1, 0] #right most bit is output bit
gates = [1, 1, 0, 0, 0, 0, 1] #right most bit corresponds to output bit, feedback gate is always closed!
n = 30 #number of cycles to run

#If gate polynomial is reducible there will be multiple isolated input states that yield varying periods and outputs, the sum of the periods will equal the max period, however

dictionary = {}
finalOutput = ""

for x in range(n):
    output = state[-1]
    feedback = 0
    foundFirstGate = False
    for i in range(len(state)-1, -1, -1):
        if(gates[i]):
            if(foundFirstGate):
                feedback = feedback ^ state[i]
            else:
                feedback = state[i]
                foundFirstGate = True
        if(i>0):
            state[i] = state[i-1]
        else:
            state[0] = feedback

    if str(state) in dictionary:
        dictionary[str(state)] += 1
    else:
        dictionary[str(state)] = 1
    finalOutput += str(output)

print("PERIOD IS: " + str(len(dictionary.keys())))
print("OUTPUT: " + finalOutput)

        