# MISC WP  我也想成为r1ngs

下载下来文件没有后缀，WinHex打开看到：

![image.png](https://i.loli.net/2019/11/02/VrvFXqMEwfQdAlK.png)

右边这些字符疑似16进制字符。尝试用如下脚本：

```python
encoded = './我也想成为r1ngs'
with open(encoded, 'r') as f:
    arr = f.read().split()

decode = []
for b in arr:
    decode.append(int(b, 16)) #转化成整数


with open('./decode', 'wb') as f:
    f.write(bytes(decode))
```

打开得到的`decode`:

![image.png](https://i.loli.net/2019/11/02/XyiHRoc8CfZrjKY.png)

可见猜想正确。

得到flag:

`Syc{Tribut3_T0_r1ngs}`

---

来自解题人的吐槽，`0`和`O`有点不确定，`9`和`g`也是，汗😓，但还是向出题人致敬！！！