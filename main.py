import base64

print('Enter your String to be encoded')
userInput = input()

#print input is optional

inputString = userInput
byteString = inputString.encode("ascii")

byteBase64 = base64.b64encode(byteString)
stringBase64 = byteBase64.decode("ascii")

print(f"Output: {stringBase64}")