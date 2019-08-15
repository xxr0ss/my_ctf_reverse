ciphertext = '437261636b4d654a757374466f7246756e'
groups = []

for i in range(0, len(ciphertext), 2):
    groups.append(ciphertext[i:i + 2])

message = ''
for group in groups:
    message += chr(int(group, 16))

print(message)