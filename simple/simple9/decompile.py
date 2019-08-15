#I made this to the style of python3 after I used uncompyle
print("Welcome to Processor's Python Classroom Part 2!\n")
print("Now let's start the origin of Python!\n")
print('Plz Input Your Flag:')
enc = input()
enc1 = []
enc2 = ''
aaa = 'ioOavquaDb}x2ha4[~ifqZaujQ#'
for i in range(len(enc)):
    if i % 2 == 0: #even
        enc1.append(chr(ord(enc[i]) + 1))
    else:  #odd
        enc1.append(chr(ord(enc[i]) + 2))

s1 = []
for x in range(3):
    for i in range(len(enc)):
        if (i + x) % 3 == 0:
            s1.append(enc1[i])

enc2 = enc2.join(s1) #get seperated parts in a list together into a string
if enc2 in aaa:
    print("You 're Right!")
else:
    print("You're Wrong!")