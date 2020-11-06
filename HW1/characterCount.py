alphabet = {}
plainFreq = {}
alphabetString = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" #treat as ciphertext
temp = "123456789<@#$%^&*()-_=+[]>"
total = 0
idx = 0
replacedText = ""

plaintext = "rteaionhsdlcumwfgypbvkzjxq".upper() #plaintext portion of the key

for c in alphabetString:
    alphabet[c] = 0
    idx += 1

file = open("HW1/input.txt", "r")
while True:
    char = file.read(1)
    if not char:
        break
    elif char.isalpha():
        alphabet[char] = alphabet[char] + 1
        total += 1
    replacedText += char

idx = 0
for key in alphabet:
    alphabet[key] = round((alphabet[key] / total) * 100, 2)
    replacedText = replacedText.replace(key, temp[idx])
    idx += 1
    

sortedByVal = sorted(alphabet.items(), key=lambda x: x[1], reverse=True)

print("Ciphertext frequencies")
idx = 0
for i in sortedByVal:
    print(i[0] + " - " + str(i[1]) + "%")
    idx+= 1

for i in range(26):
    replacedText = replacedText.replace(temp[i], plaintext[i])
    plainFreq[plaintext[i]] = alphabetString[i]

print("\n\nPlaintext -> Ciphertext - Frequency")
sortedKeys = sorted(plainFreq.keys())
for key in sortedKeys:
    print(key + " -> " + plainFreq[key] + " - " + str(alphabet[plainFreq[key]]) + "%")

print(replacedText)