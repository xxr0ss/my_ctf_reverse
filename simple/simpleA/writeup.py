# 比较简单，就不写markdown了，直接pycdc得到python源码如下：

"""
import string
letters = list(string.letters) + list(string.digits) + ['+', '/']
dec = 'FcjTCgD1EffEm2rPC3bTyL5Wu2bKBI9KAZrwFgrUygHN'

def encode(input_str):
    str_ascii_list = [ ('{:0>8}').format(str(bin(ord(i))).replace('0b', '')) for i in input_str ]
    output_str = ''
    equal_num = 0
    while str_ascii_list:
        temp_list = str_ascii_list[:3]
        if len(temp_list) != 3:
            while len(temp_list) < 3:
                equal_num += 1
                temp_list += ['00000000']

        temp_str = ('').join(temp_list)
        temp_str_list = [ temp_str[x:x + 6] for x in [0,6,12,18]]
        temp_str_list = [ int(x, 2) for x in temp_str_list ]
        if equal_num:
            temp_str_list = temp_str_list[0:4 - equal_num]
        output_str += ('').join([ letters[x] for x in temp_str_list ])
        str_ascii_list = str_ascii_list[3:]

    output_str = output_str + '=' * equal_num
    return output_str


print "Now let's start the origin of Python!\n"
print 'Plz Input Your Flag:\n'
enc = raw_input()
lst = list(enc)
lst.reverse()
llen = len(lst)
for i in range(llen):
    if i % 2 == 0:
        lst[i] = chr(ord(lst[i]) - 2)
    lst[i] = chr(ord(lst[i]) + 1)

enc2 = ''
enc2 = enc2.join(lst)
enc3 = encode(enc2)
if enc3 == dec:
    print "You're right! "
else:
    print "You're Wrong! "
# okay decompiling .\simple10.pyc
"""

# letters一看就和base64有关，通过测试发现就是个base64变表，大小写换了下，其他没变

# 用python3写解题脚本
import string
from base64 import b64decode

letters = string.ascii_letters + string.digits + '+/'
std_table = string.ascii_uppercase + string.ascii_lowercase + string.digits + '+/'

def decode(data: str):
    trans = str.maketrans(letters, std_table)
    data = data.translate(trans).encode()
    return b64decode(data)


dec = 'FcjTCgD1EffEm2rPC3bTyL5Wu2bKBI9KAZrwFgrUygHN'
enc3 = decode(dec)

lst = list(enc3)
for i in range(len(lst)):
    lst[i] = lst[i] - 1
    if i % 2 == 0:
        lst[i] = lst[i] + 2

lst.reverse()
print(bytes(lst).decode())