RE WP Python1

用uncompyle得到源码后稍微修改一下得到如下代码：

```python
import struct, time

def b(a):
    return a & 18446744073709551615


def c(str):
    return struct.unpack('<Q', str)[0]


def d(a):
    for i in range(64):
        a = a * 2
        if a > 18446744073709551615: #0xffffffffffffffff,即int64溢出
            a = b(a)
            a = b(a ^ 12682219522899977907)

    return a


if __name__ == '__main__':
    cmp_data = [
     7966260180038414229, 16286944838295011030, 8598951912044448753, 7047634009948092561, 7308282357635670895]
    input = raw_input('plz input your flag:')
    if len(input) % 8 != 0:
        for i in range(8 - len(input) % 8):
            input += '\x00'

    arr = []
    for i in range(len(input) / 8):
        value = d(c(input[i * 8:i * 8 + 8]))
        arr.append(value)

    for i in range(5):
        if arr[i] != cmp_data[i]:
            print 'fail'
            time.sleep(5)
            exit()

    print 'success'
    time.sleep(5)
    exit()
```

仔细观察发现`d()`里面的for循环里，如果a * 2即a << 1，如果左移完了之后**最后一位是0(b)**，如果a本来最高位是`1`(b)，左移后就会和`0xffffffffffffffff`进行&操作**并且**与`12682219522899977907`异或一下，关键点是：

`12682219522899977907 == 0b1011000000000000010010110111011001111001111110100010011010110011 `

（**最后一位**是1(b))

所以这64次循环里，可以通过结尾位是0还是1来判断`a << 1`前最高位是0还是1，进而推断`a`传入函数`d()`前本来是多少。

则可得以下解题脚本：

```python
ciphers = [0x6e8dd76d3b876f95, 0xe206da09daf4bed6,
           0x77559d346e134bf1, 0x61ce39cac5eaf891,
           0x656c3c155520e36f]

def decode(a):
    xor = 0xb0004b7679fa26b3
    for i in range(64):
        if a & 1 == 1: #对最后一个bit判断是否为1
            a ^= xor
            a += 0xffffffffffffffff + 1
            a = a>> 1
        else:
            a = a >> 1
    return a

def toStr(a):
    tmp = hex(a)[2:]
    ans = ''
    for i in range(len(tmp) // 2):
        ans += chr(int(tmp[i*2: i*2 + 2], 16))
    return ans

ans = []
for cipher in ciphers:
    decoded = decode(cipher)
    ans.append(toStr(decoded)[::-1]) #'<Q'是小端模式

print(''.join(ans))
```

得flag:

`Syc{L1fe_i5_sh0rt_y0u_n3ed_py7h0n}`