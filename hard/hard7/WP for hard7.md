# WP for hard7

![status](https://img.shields.io/badge/status-incomplete-red)

FYI:本题涉及内容较多，请先自行了解ELF文件IDA远程调试（非必须，但极大地方便解题），z3库的使用（我用的是Python3），[花指令](https://github.com/pjx206/pjx_ctf_reverse/blob/master/Note/%E8%8A%B1%E6%8C%87%E4%BB%A4.md)，SMC自解密

虚拟机环境: Kali Linux 64-bit（Ubuntu 18.04不支持32位程序，装32位运行库也相当麻烦）

## 程序逻辑

* 先读入两个数（可以理解为Key）

* 用一个函数对这两个数进行判断，如果符合条件，才能进行输入flag。

* 由一个函数B解密“用来检验flag的A函数”

* 用A函数检验flag的正确性

然而第二步不能简单通过爆破绕过对这两个数的判断，因为处理输入的flag的函数A被加密了，而解密这个A函数的B函数，以这两个数作为密钥，对A函数的加密代码进行解密。

## 解题思路

### 0x00 去除花指令

IDA打开可以看到

![image.png](https://i.loli.net/2019/10/02/35C9vsgwoGAprEV.png)

对应的汇编代码是没有被IDA分析出来函数的，仔细寻找

```
jb  xxx
jnb xxx
```

这样的花指令，用类似

```Python
addr = 0x08048771
for i in range(4):
    PatchByte(addr + i, 0x90)
```

的脚本Patch掉花指令，然后对非垃圾数据按<kbd>C</kbd>来重新分析，当花指令去除得差不多的时候，用<kbd>P</kbd>创建函数，最终得到main函数长这样

