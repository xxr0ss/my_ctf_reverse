key = [160, 230, 122, 286, 230, 144, 290, 208, 240,
       144, 300, 216, 290, 244, 240, 100, 256, 310]

flag = ''
for i in range(18):
    for j in range(32, 127):
        a = (j>>4) & 0xF
        b = (16*j >> 4) & 0xF
        if (a * 22 + b * 12) == key[i]:
            flag += chr(j)

print(flag)