# RE WP  Dll Reverse

首先IDA打开，反编译一下，注意一下`_setup0.dll`文件不要搞丢了，不缺失这个dll的话，程序会运行到

```c
if (v5)
{
	v7 = GetProcAddress(v5, "_TRocMxlr");
	if (!v7)
		printf_s("Cannot load important file! Please restart the program and check permission.\n");
	if (((unsigned __int8(__cdecl*)(char*))v7)(v0))
		printf_s("Perfect! You Get the flag!\n");
	else
		printf_s("Worry!Just try it again.\n");
	v6 = hLibModule;
}
```

这个`((unsigned __int8(__cdecl*)(char*))v7`就是在调用`_setup0.dll`并传入参数`v0`(也就是输入）

---

IDA打开`_setup0.dll`：

`sub_10001028`就是处理输入的函数了，

函数前面的部分很明显是base64编码过程，主要体现在：

* 右移位操作
* 有一个包含64个字符的数组
* 必要的话对结尾进行补`=`操作（`chr(0x3d) == '='`)

**注意一点：**编码用的表不是标准表，而是：`ABCDEFGHIJKLMNOPQSVXZRWYTUeadbcfghijklmnopqrstuvwxyz0123456789+/`

反汇编的伪代码里面处理完base64后

```c
v13 = b64 - aEjc4vOggcCulgE;
do
{
	chr = aEjc4vOggcCulgE[v13 + i];
	if (i % 2)                                // i奇数
		v15 = aEjc4vOggcCulgE[i] ^ chr;       // 后面脚本里我把这个作为key
	else
		v15 = (aEjc4vOggcCulgE[i] ^ chr) + 3;
	byte_10003390[i++] = v15;
}
```

我改了变量命名，这里就是用chr来暂存base64变表编码后的每一个字符，我也没看懂第一行减字符串地址是啥操作，动态调试才发现`chr = aEjc4vOggcCulgE[v13 + i]`把每个编码后字符拿出来了，然后就是按奇偶操作了一下，最后就是：

```c
while ( i < 32 );
j = 0;
while ( byte_10003390[j] == byte_10003034[j] )
{
    if ( ++j >= 32 )
        return 1;
}
```

前面步骤处理完后和后面这个`byte_10003034`每一位字符比较，这里解题脚本我就直接把它当cipher了：

解题脚本：

```python
import base64

cipher = [34, 89, 50, 94, 56, 11, 66, 86, 38, 112, 77, 69, 19, 34, 45, 29, 91, 55, 112, 3, 18, 96, 124, 54, 7, 83, 3, 83, 79, 120, 86, 38]
key = [69, 106, 67, 52, 86, 59, 79, 103, 71, 67, 25, 35, 67, 117, 108, 103, 59, 101, 84, 70, 66, 55, 1, 80, 85, 96, 73, 36, 24, 74, 39, 31, 9, 29, 74, 0] #内存中有挺多位的，实际上这里只要用32个就行

tmp = []
for i in range(len(cipher)):
    if i % 2 == 1:
        tmp.append(cipher[i] ^ key[i])
    else:
        tmp.append((cipher[i] - 3) ^ key[i])
        

std = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
nstd = 'ABCDEFGHIJKLMNOPQSVXZRWYTUeadbcfghijklmnopqrstuvwxyz0123456789+/' #非标准表


trans = str.maketrans(nstd, std)
tmp = ''.join(map(chr, tmp))
tmp = tmp.translate(trans) #转化成标准编码形式

flag = base64.b64decode(tmp)
print(flag)
```

得到flag:

`Syc{Just_Easy_D1l_Cr0ck}`