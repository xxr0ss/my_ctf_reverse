和simple4.exe套路类似，加密一段字符，结果放在某个地方，先找到加密的字符串，再分析加密过程，得到解密方法，得到flag。
`FZQ{HAVE_A_GOOD_TIME_!}`

解密代码：
```python
ciphertext = [85, 15, 94, 37, 109, 44, 122, 63, 96, 33, 126,
       57, 118, 57, 125, 34, 118, 63, 114, 55, 104, 73, 52]

message = ''
key = 19
for i in range(len(ciphertext)):
    message += chr(ciphertext[i] ^ key)
    key = ciphertext[i]

print (message)
```