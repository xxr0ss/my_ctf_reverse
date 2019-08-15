先利用在线工具将simple3.pyc反编译，得到下面的**decompile_ref.py**

发现是python2写的，稍微修改

注意`return base64.b64encode(s)`修改为`return base64.b64encode(s.encode('utf-8'))`

得到python3可运行的代码
***
分析。。。

![party-bird](https://emojis.slackmojis.com/emojis/images/1471119458/990/party_parrot.gif?1471119458)
得到我们的解密代码：
```python
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
```

运行得出flag：
`nctf{d3c0mpil1n9_PyC}`