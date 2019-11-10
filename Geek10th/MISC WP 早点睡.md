# MISC WP 早点睡

所用软件：

* Adobe Photoshop CC 2019
* WinHex
* Visual Studio Code
* Chrome

题目压缩包解压得到一个`sleep1.png`，体积很大，而且WinHex打开是没有PNG该有的文件头部和尾部的，但是不难看到ANSI ASCII窗口有有关Adobe的东西。

```
Offset      0  1  2  3  4  5  6  7   8  9  A  B  C  D  E  F
00000000   38 42 50 53 00 01 00 00  00 00 00 00 00 03 00 00   8BPS            
00000010   04 38 00 00 05 A0 00 08  00 03 00 00 00 00 00 00    8   ?         
00000020   61 0A 38 42 49 4D 04 04  00 00 00 00 00 1F 1C 01   a 8BIM          
00000030   5A 00 03 1B 25 47 1C 01  5A 00 03 1B 25 47 1C 01   Z   %G  Z   %G  
00000040   5A 00 03 1B 25 47 1C 02  00 00 02 00 00 00 38 42   Z   %G        8B
00000050   49 4D 04 25 00 00 00 00  00 10 D3 C9 9F 4B 3D 8D   IM %      由烱= 
00000060   EA 28 85 48 35 6A 84 15  9C 2B 38 42 49 4D 04 24   ?匟5j??8BIM $
00000070   00 00 00 00 3E CE 3C 3F  78 70 61 63 6B 65 74 20       >??xpacket 
00000080   62 65 67 69 6E 3D 22 EF  BB BF 22 20 69 64 3D 22   begin="锘? id="
00000090   57 35 4D 30 4D 70 43 65  68 69 48 7A 72 65 53 7A   W5M0MpCehiHzreSz
000000A0   4E 54 63 7A 6B 63 39 64  22 3F 3E 0A 3C 78 3A 78   NTczkc9d"?> <x:x
000000B0   6D 70 6D 65 74 61 20 78  6D 6C 6E 73 3A 78 3D 22   mpmeta xmlns:x="
000000C0   61 64 6F 62 65 3A 6E 73  3A 6D 65 74 61 2F 22 20   adobe:ns:meta/" 
000000D0   78 3A 78 6D 70 74 6B 3D  22 41 64 6F 62 65 20 58   x:xmptk="Adobe X
000000E0   4D 50 20 43 6F 72 65 20  35 2E 36 2D 63 31 33 38   MP Core 5.6-c138
000000F0   20 37 39 2E 31 35 39 38  32 34 2C 20 32 30 31 36    79.159824, 2016
00000100   2F 30 39 2F 31 34 2D 30  31 3A 30 39 3A 30 31 20   /09/14-01:09:01 
```

足以说明文件没有被加密，百度8BPS，第一条就看到这个：

> 8BPS文件整么打开
> 8BPS文件打开方式?*8BPS*文件扩展名信息 一种Photoshop文件。推荐文件扩展名 DFN ASC JIF MSSTYLES BIP GRH R53 W91 AAM CRF DDT POP ZOH P65 2GR DXN ZOM POF...

进一步确认是PS可打开的一种文件格式。

将`sleep1.png`修改后缀得到`sleep1.psd`，PS果然能打开并得到肖学姐的照片（不知道Lamber师傅从哪得来的👀）。

调整下两个图层的透明度和填充，可以得到如下图片

![image.png](https://i.loli.net/2019/11/06/h3b6UrgJxAi94Co.png)

---

下载解压得到sleep2.png，有一次，不是PNG，文本打开得到

```
iVBORw0KGgo...
```

这个开头是常见的**base64转图片**，这里给出一个我自用的模板（也可以找在线base64转图片网站）

```html
<!DOCTYPE html>
<html>
    <img src="data:image/png;base64,iVBORw0KGgo(填base64编码)"/>
</html>
```

考虑到篇幅问题，不放出完整代码，`sleep2.png`中的base64编码得到的是一个二维码图片，扫描，下载，`sleep3.zip`同样的套路。

...

---

`sleep4.zip`解压，文本打开，尝试同样方法发现图片不能正常显示，遂检查，发现编码中间出现`=`（标准base64只在结尾会出现`=`），于是用如下脚本处理：

```python
with open('./sleep4.png', 'r') as f:
    chars = f.read()

chars = chars.replace('=','')
with open('./processed_sleep4', 'w') as f:
    f.write(chars)
```

处理完的字符串（结尾自行补两个`=`，这个脚本会去掉所有的`=`）用我的那个模板得到

![image.png](https://i.loli.net/2019/11/06/ScZWTxXCRzgApe3.png)

奇奇怪怪的图片，先右键保存，WinHex打开

```
Offset      0  1  2  3  4  5  6  7   8  9  A  B  C  D  E  F

000001B0   1C 39 22 C7 8F 1F 97 37  BF 53 79 63 7B 53 74 61    9"? ?縎yc{Sta
000001C0   79 69 6E 67 5F 55 70 6C  61 74 65 5F 49 53 5F 62   ying_Uplate_IS_b
000001D0   61 64 66 6F 72 5F 54 68  65 42 6F 64 79 7D 05 37   adfor_TheBody} 7
000001E0   96 37 B5 37 46 17 96 96  E6 75 F5 57 06 C6 17 46   ??F 枛鎢鮓 ?F
000001F0   55 F4 95 35 F6 26 16 46  66 F7 25 F5 46 86 54 26   U魰5? Ff?鮂員&
00000200   F6 47 97 D0 53 79 63 7B  53 74 61 79 69 6E 67 5F   鯣椥Syc{Staying_
00000210   55 70 6C 61 74 65 5F 49  53 5F 62 61 64 66 6F 72   Uplate_IS_badfor
00000220   5F 54 68 65 42 6F 64 79  7D 05 37 96 37 B5 37 46   _TheBody} 7??F
00000230   17 96 96 E6 75 F5 57 06  C6 17 46 55 F4 95 35 F6    枛鎢鮓 ?FU魰5?
00000240   26 16 46 66 F7 25 F5 46  86 54 26 F6 47 97 D0 53   & Ff?鮂員&鯣椥S
00000250   79 63 7B 53 74 61 79 69  6E 67 5F 55 70 6C 61 74   yc{Staying_Uplat
00000260   65 5F 49 53 5F 62 61 64  66 6F 72 5F 54 68 65 42   e_IS_badfor_TheB
00000270   6F 64 79 7D 05 37 96 37  B5 37 46 17 96 96 E6 75   ody} 7??F 枛鎢
```

原来那些点点就是flag，flag在整个图片中随处可见。

得flag：

`Syc{Staying_Uplate_IS_badfor_TheBody}`

---

Lamber师傅幸苦了，另外，WP写起来也挺累的😵