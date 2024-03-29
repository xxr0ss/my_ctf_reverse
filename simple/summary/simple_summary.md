# 对这些简单题的总结

## 0x01 大小端模式：

数据储存的时候是有[大小端模式]([https://baike.baidu.com/item/%E5%A4%A7%E5%B0%8F%E7%AB%AF%E6%A8%A1%E5%BC%8F/6750542?fr=aladdin#1](https://baike.baidu.com/item/大小端模式/6750542?fr=aladdin#1))之分的。根据百度百科：

> 为什么会有大小端模式之分呢？这是因为在计算机系统中，我们是以字节为单位的，每个地址单元都对应着一个字节，一个字节为 8bit。但是在C语言中除了8bit的char之外，还有16bit的short型，32bit的long型（*要看具体的编译器*），另外，对于位数大于 8位的处理器，例如16位或者32位的处理器，由于寄存器宽度大于一个字节，那么必然存在着一个如何将多个字节安排的问题。因此就导致了大端存储模式和小端存储模式。例如一个16bit的short型x，在内存中的地址为0x0010，x的值为0x1122，那么0x11为高字节，0x22为低字节。对于 大端模式，就将0x11放在低地址中，即0x0010中，0x22放在高地址中，即0x0011中。小端模式，刚好相反。我们常用的X86结构是小端模式，而KEIL C51则为大端模式。很多的ARM，DSP都为小端模式。有些ARM处理器还可以随时在程序中(在ARM Cortex 系列使用REV、REV16、REVSH指令)进行大小端的切换。

在simple2中，用IDA得到的![key](./simple2_key.png)

转换成16进制，每两位为一个字符(char占1byte)，看了[《汇编语言》](https://book.douban.com/subject/25726019/)（王爽）的应该清楚，一个字符储存在一个8bits的内存单元，储存的时候这个v7代表的字符串的字符是小端储存，所以转成16进制的整数再两位两位分开得到一个个字符拼成的字符串是倒序的。

> 一般来说，x86 系列CPU都是 Little-endian 字节序，PowerPC 通常是 Big-endian 字节序。因为网络协议也都是采用 Big-endian 方式传输数据的，所以有时也把 Big-endian 方式称为网络字节序。

## 0x02 Python果然很重要

这些简单题大多是加密字符串的题，写写Python脚本解题真的很方便，常见套路是进行一些[位操作](https://www.luogu.org/blog/chengni5673/er-jin-zhi-yu-wei-yun-suan)再加上其他运算，得到密文，分析一下加密的过程，有的可以逆推得到解密的公式，有的逆推不出就只能暴力破解了，一个小技巧是ASCII里33号到126号的可见字符才会出现在flag里边，所以不要从0循环到127，节省一点运算时间。

另外就是，好多题是用Python2出的是吧，用`uncompyle`反编译一下是一堆python2代码，一般改改print()就可以，有时候也有其他函数在python2和python3有小区别。我学的是python3，但目前可以靠搜索来补充我不知道的关于python2的东西。

## 0x03 数据类型&指针

可以看出基础还是很重要的，各式各样的数据类型转换，指针算术，让我意识到我的基础还不扎实，反编译完了挺多各种各样的`int`和什么`_BYTE`啥的确实不知道是啥，一些C里面的函数也没见过，~~有时候没注意到指针算术，看半天不知道那原来就是个数组。~~可见基础不好。

## 0x04 耐心，眼尖

有的flag是**明文**储存的，16进制打开好好看下，能发现意想不到的有用信息，有时候是flag，有时候是加壳的类型。

另外就是透过现象看本质，比如有时候一大堆的位操作其结果却很简单，比如`>>`一个比较大的数，其结果往往就是0而已。`a & 31`这样的，其实a(<=31)与0b1111与操作完了还是a本身。

# 0x05 其他

在python3中`base64.b64decode()`返回值是`bytes`类型，所以要对其用`for-in`把每一个元素转化成`chr`类型。拼接起来成字符串。