# PWN WP find tools

`nc pwnto.fun 9999`有个东西一闪而过，就让你输入key，所以还是要靠特殊方法比如录视频（2333），或者用python的pwntools

![1570884395247.png](https://i.loli.net/2019/10/16/Mn25YBICRUr3eNv.png)

这个key有个`=`表明应该是base64加密的

解密一下：

![1570884507457.png](https://i.loli.net/2019/10/16/CMcUV1bDv7WdqZn.png)

然而控制台输入的时候：

![1570884559211.png](https://i.loli.net/2019/10/16/ecILrMsk5qnhUTV.png)

所以继续上python：

![1570884612584.png](https://i.loli.net/2019/10/16/UF7fd3Ayb6jVKDh.png)

得到flag:`Syc{pwn_1s_s0_fun}`