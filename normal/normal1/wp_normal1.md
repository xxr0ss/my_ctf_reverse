**flag:C1CTF{th1s_Bas364_is_qcjlCwgS}**



IDA打开，看到`main()`中读入输入的flag到v5后对奇偶位的每个字符分别进行了异或运算

```C
__isoc99_scanf("%60s", v5);
for ( i = 0; i < strlen(v5); ++i )
{
    if ( i & 1 )
      v5[i] ^= 0x60u;
    else
      v5[i] ^= 0x91u;
}
```

然后经过`sub_A84(v5, &s2)`处理把结果放到s2数组里面了

---

在`sub_A84(v5, &s2)`中，有一个没有参数的`sub_7FA()`，进行一个有64个case的跳转，每个case返回的字符和标准的base64编码表是对应不上的，这里其实是一个变表，通过汇编代码可以看出

![image.png](https://i.loli.net/2019/10/03/LuPx6VfdNmtQcyE.png)的这个off_D94其实就是`sub_A84(v5, &s2)`中![image.png](https://i.loli.net/2019/10/03/UjMTakeDKPoL3sJ.png)

的v2。

程序的逻辑就分析到这。

---

解题脚本

```python
import base64

ciphertext = 'OBufaa21Td86rWS8Wob8iGhZYocbr5vxZfcCoWv3'
std = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'     #标准编码表
changed = 'nopqrstuvwxyzabcdefghijklm0123456789ABCDEFGHIJKL+/MNOPQRSTUVWXYZ' #变表

#得到如果用标准表编码应该得到的base64码
trans = str.maketrans(changed, std)
ciphertext = ciphertext.translate(trans)

#base64解码
ciphertext = bytes(ciphertext, encoding='utf-8')
arr = base64.b64decode(ciphertext)

#对异或操作进行还原
flag = ''
for i in range(len(arr)):
    c = arr[i] ^ 0x91 if i % 2 == 0 else arr[i] ^ 0x60
    flag += chr(c)


print(flag)
#OUT:C1CTF{th1s_Bas364_is_qcjlCwgS}
```

