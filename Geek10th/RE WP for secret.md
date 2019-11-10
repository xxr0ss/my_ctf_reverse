# RE WP for secret

IDA打开，`main()`里面后面是有一个比较，用来比较的字符串一看就知道是那种常见的两位两位16进制为一个字符的，解题脚本：

```python
s = '5379637B6E30775F794F755F6B6E6F775F6234736531367D'
for i in range(len(s)//2):
    print(chr(int(s[i*2: i*2 + 2], 16)), end='')
```

flag:`Syc{n0w_yOu_know_b4se16}`