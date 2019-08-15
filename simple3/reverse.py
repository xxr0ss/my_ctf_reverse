import base64

def decode(ciphertext):
    b64_decode = base64.b64decode(ciphertext)
    
    message = ''
    for c in b64_decode:
        x = c - 16
        x = x ^ 32
        message += chr(x)

    return message

ciphertext = 'XlNkVmtUI1MgXWBZXCFeKY+AaXNt'
print('flag:'+decode(ciphertext))