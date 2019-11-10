# RE Easy VB WP

话说逆向七分分析三分猜。（我好菜啊！）

本题我卡在调试上，程序会启动多个线程，在OD里面把`Main`以外的线程suspend掉使调试能继续进行。

断点下载`0x00402395`（后面有个`__vbaStrCmp`，把加密后的字符串与`bKPObQ@goYBGRXjtVKVSn^@kFQh[V_]O`比较是否相同。

大致猜测flag长度是32（毕竟其他位数的flag好像调试总有问题，然后有一个字符串（设为key）`12345a789012345678g012345a789012`长度也是32，用来和输入进行一些操作）。

用python输出`'A' * 32`，`'B' * 32`，输入输入框测试发现，比如是32个`A`的时候，执行到`0x00402395`时，ECX存的地址底下（处理过的输入字符串）是`psrut vyxqpsrutwvy&qpsrut vyxqps`，猜测和证实发现这个字符串是输入字符串每一位和key异或后得到的。

得解题脚本

```python
cipher = 'bKPObQ@goYBGRXjtVKVSn^@kFQh[V_]O'
key = '12345a789012345678g012345a789012'
flag = ''
for i in range(32):
    flag += chr(ord(key[i]) ^ ord(cipher[i]))
print(flag)
```

输出：`Syc{W0w_Visual_Bas1c_ls_s0_cool}`

