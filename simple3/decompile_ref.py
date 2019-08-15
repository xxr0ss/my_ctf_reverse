import base64
 
def encode(message):
    s = ''
    for i in message:
        x = ord(i) ^ 32
        x = x + 16
        s += chr(x)
 
    return base64.b64encode(s.encode('utf-8'))
 
 
correct = ('XlNkVmtUI1MgXWBZXCFeKY+AaXNt')
flag = ''
flag = input("Input flag:")
if encode(flag) == correct:
    print('correct')
else:
    print ('wrong')