# ReversingKr KeygenMe
# Find the Name when the Serial is 5B134977135E7D13

ciphertext = [0x5B, 0x13, 0x49, 0x77, 0x13, 0x5E, 0x7D, 0x13]
key = [0x10, 0x20, 0x30]

message = ''
for i in range(len(ciphertext)):
    message += chr(ciphertext[i] ^ key[i % 3]) # 3 is the length of the key 

print(message)
