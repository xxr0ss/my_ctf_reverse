**反编译**，得到：
![avatar](decompile.png)

看到关键字符串`'437261636b4d654a757374466f7246756e'`,
注意到line:36是字符串比较，所以这个题要找加密前的flag。

**加密部分**为line:27 到 line:35,其原理是把字符转化成16进制整数再存成字符串。

可得**解密过程：**

把那个长长的字符串两个为一组(16进制两位数储存一个字符)，分别还原原来的字符得到解密脚本
```
ciphertext = '437261636b4d654a757374466f7246756e'
groups = []

for i in range(0, len(ciphertext), 2):
    groups.append(ciphertext[i:i + 2])

message = ''
for group in groups:
    message += chr(int(group, 16))

print(message)
```
