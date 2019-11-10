# MISC WP 嘿，你喜欢吃鲱鱼罐头吗？ 

题目下载下来是个伪加密的zip，解压得到一张jpg图片

16进制打开，发现有一段非常诡异的由`i` `s` `d` `o`组成的字符串，查看jpg的属性，备注中有

> 它看起来就像是死鱼一样

根据题目提示，在Google上查找了关键字`deadfish`，看到这个结果：

![image.png](https://i.loli.net/2019/11/10/XfrkAnICa29MxUG.png)

![image.png](https://i.loli.net/2019/11/10/AwsN7BMYC4egalK.png)

可见`deadfish`是解题关键，在GitHub上能找到[这个](https://github.com/craigmbooth/deadfish) 

根据readme，可见只要通过这个得到flag就行。

下载下来在该目录运行以下脚本：

```python
import deadfish

fish = 'iisiiiisiiiiiiiiiiiiiiiiiiioiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiioddddddddddddddddddddddoiiiiiiiiiiiiiiiiiiiiiiiioddddddddddddddddddddddddddddddddddddddddoiiodddoioioddoddddddddddddddddddddddddddddddddddoiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiooddddoiiiiiodddddddoddddddddoiiiiiiiiiioiiiiiiiiiioddddddddddddddddddddoiiiiioiodddddddddddddddddddddddddoiiiiiiiiiiiiiiiiiiiiiiiiiiiiioddddddoiiiiiiodddddddddddddddddddddddddddddddddddddddddddddddddddddddddoiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiioddoiiiiiiiiiio'
fish = fish.split('o')

flag = ''
for i in range(len(fish)):
    tmp = ''.join(fish[:i])
    tmp = deadfish.deadfish(tmp) & 0xff
    flag += chr(tmp)

print(flag)

```

得到flag：

`Syc{SURSTR0mming_is_deLici0us}`

---

PS：出题人脑洞太大了！膜拜！