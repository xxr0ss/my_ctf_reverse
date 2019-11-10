# RE WP 冰菓

![1571060518335.png](https://i.loli.net/2019/10/16/2jrepYs7VnGTIqb.png)

dnSpy打开，注意到EncryptStr，进去看到加密代码，比较简单。

解密代码：

```python
arr = [119, 77, 103, 79, 21, 115, 133, 97, 115, 87, 22, 115, 103, 89, 88, 93, 22, 89, 119, 81]
for i in range(20):
    print(chr((arr[i] - 13) ^ 57), end='')
```

flag:`Syc{1_Am_s0_curi0uS}`