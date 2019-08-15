ciphertext = [85, 15, 94, 37, 109, 44, 122, 63, 96, 33, 126,
       57, 118, 57, 125, 34, 118, 63, 114, 55, 104, 73, 52]

message = ''
key = 19
for i in range(len(ciphertext)):
    message += chr(ciphertext[i] ^ key)
    key = ciphertext[i]

print (message)