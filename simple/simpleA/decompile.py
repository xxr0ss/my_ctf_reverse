import string
letters = list(string.letters) + list(string.digits) + ['+', '/']
dec = 'FcjTCgD1EffEm2rPC3bTyL5Wu2bKBI9KAZrwFgrUygHN'


def encode(input_str):
    str_ascii_list = [('{:0>8}').format(
        str(bin(ord(i))).replace('0b', '')) for i in input_str]
    output_str = ''
    equal_num = 0
    while str_ascii_list:
        temp_list = str_ascii_list[:3]
        if len(temp_list) != 3:
            while len(temp_list) < 3:
                equal_num += 1
                temp_list += ['00000000']

    lst[i] = chr(ord(lst[i]) + 1)


enc2 = ''
enc2 = enc2.join(lst)
enc3 = encode(enc2)
if enc3 == dec:
    print("You're right! ")
else:
    print("You're Wrong! ")
