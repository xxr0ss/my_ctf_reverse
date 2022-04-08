

# hard12 步骤记录

2019.10.07

识别出`.rodata:0000000000400D40`应该是虚拟机的操作码。

---

确定了一个函数功能 但没判断出`eax`和`edx`相当于哪个虚拟寄存器

---

**留意一下VM的结构：**

> - **VM_DATA** 是虚拟机字节码，是虚拟机要解释执行的指令。
> - **VM_EIP**，也可以叫 VPC 或者 vEIP ，比如 VMProtect 中的 ESI 寄存器。一般是指向 VM_DATA 中的某个地址，虚拟机每次从这里取出指令，并执行。
> - **VM_CONTEXT** 虚拟机上下文，实际就是虚拟机寄存器数组。比如 VMProtect 中的 EDI 寄存器的地址，就是虚拟机寄存器数组的起始地址。
> - **VM_STACK** 虚拟栈，栈式虚拟机实现起来方便，膨胀倍数高，是虚拟机保护的首选。虚拟栈就是临时进行数据交换。VMProtect 的 EBP 寄存器就是虚拟栈的栈顶指针。

---

2019.10.07

确认了vEIP了，是地址`.bss:0000000000602084`处的一个字节，其实感觉更应该是vIP，因为寄存器只有八位嘛。不过感觉这样似乎提供了一个重要信息，**虚拟机的寄存器大小**。

也确认了几个函数/handler的功能，下一步就是慢慢推测出全部来。

---

留意到虚拟机指令是按BYTE给虚拟机的，可以初步认为虚拟机就是16位的。

---

快要猜测完毕虚拟机的寄存器了，注意到那个类似虚拟机解释器的函数里`.text:0000000000400A4F`里面有如下内容：

（图片无了）

判定该函数应该是`vPUSH`，而且压入的是一个字节，而且还能进一步确认`r_d`是维护虚拟栈的指针`esp`还是`ebp`嘞？我有点菜两个指针还没完全搞懂，好像是`ebp`。然后那个应该是栈的地址，不是栈，毕竟只有一个字节怎么可能储存一整个栈嘛hhh，嗯应该是了。

---

感觉寄存器的分析还是有点迷糊，然后虚拟解释器的第一个`switch`有点意思，要留意一下。

---

意识到对`vPUSH`和`vPOP`分析可能弄反了，还没搞清楚虚拟栈的延伸方向是向高位还是低位。

---

还是感觉没错，根据参数类型可以进行一定的判断，之前判断的比如第二个`switch`的`case 0u`，以及开始的那几个，是对**内容**（与地址区分开）的操作，何况`line32: v6 = *(_BYTE *)(v2 + opcode_arr);`这个v6不可能是指针呀。这些看起来是`vPUSH`的函数，把参数放到了`vSTACK`向高位延伸的地方，进一步推断虚拟栈延伸方向向高位进行拓展。

---


实锤了，那个确实是虚拟栈，虚拟栈的延伸方向确实是向高位延伸。

---

就这个题而言，现在估计是人肉逆向比较快。

---

目前来讲，handler已经分析完毕，emmm人肉逆向开始：

---

分析中：

判断r_c寄存器作用：读入flag的字符串长度的计数器



---

很好，我是一个没有感情的逆向机器：

```
addr |   hex    |  cmd
0x00  0x11 0x2D   push eip & jmp 0x2D
0x02  0x00 0x22   push 0x22
0x04  0x05        pop r_b
0x05  0x10        cmp r_a, r_b
0x06  0x14 0x09   je 0x09
0x08  0x17        exit

0x09  0x00 0x32   push 0x32
0x0B  0x05        pop r_b
0x0C  0x03        push r_c
0x0D  0x11 0x16   push eip & jmp 0x16
0x0F  0x06        pop r_c
0x10  0x00 0x16   push 0x16
0x12  0x05        pop r_b
0x13  0x11 0x16   push eip & jmp 0x16
0x15  0x17        exit

0x16  0x0E 0x01   sub r_c, 1
0x18  0x15        push s[r_c]
0x19  0x04        pop r_a
0x1A  0x0F        xor r_a, r_b
0x1B  0x01        push r_a
0x1C  0x16        pop str[r_c]
0x1D  0x02        push r_b
0x1E  0x00 0x00   push 0
0x20  0x04        pop r_a
0x21  0x03        push r_c
0x22  0x05        pop r_b
0x23  0x10        cmp r_a, r_b
0x24  0x14 0x2B   je 0x2B

0x26  0x05        pop r_b
0x27  0x09 0x03   add r_b, 0x03
0x29  0x13 0x16   jmp 0x16

0x2B  0x05        pop r_b
0x2C  0x12        pop eip

0x2D  0x15        push s[r_c]
0x2E  0x04        pop r_a
0x2F  0x10        cmp r_a, r_b
0x30  0x14 0x36   je 0x36
0x32  0x0A 0x01   add r_c, 1
0x34  0x13 0x2D   jmp 0x2D
0x36  0x03        push r_c
0x37  0x04        pop r_a
0x38  0x12        pop eip
```

---

发现上面代码中0x11 xxx虚拟指令其实还会先vEIP入栈（现在已经修改了）

---

感觉吧，只要输入flag长度为34就行，所以可以跟踪一下，搞清楚加密过程



---

人肉逆向，完事


加密逻辑比较简单，大概就是如下加密过程：

```python
s = 'xxxxxxxx' #len == 34
t = 0x32
for i in range(len(s)):
    s[i] ^= t
    t += 3

t = 0x16
for i in range(len(s)):
    s[i] ^= t
    t += 3
#get the ciphertext
```

