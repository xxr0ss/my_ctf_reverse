WP Simple14

IDA打开，找不到`main()`，于是<kbd>shift</kbd>+<kbd>F12</kbd>查找字符串，确认程序主要部分在`sub_1400010E0()`中。

伪代码中前面一部分看上去应该是应对调试器的部分，先不管。

```c
v6 = v21;
  v7 = 26i64;
  do
  {
    sub_140001080("%d", v6);
    --dword_140005034;
    ++v6;
    --v7;
  }
  while ( v7 );
  v8 = 0i64;
  v9 = 0i64;
  v10 = 0i64;
  v11 = 0i64;
  v12 = 0i64;
  do
  {
    switch ( v21[v9] )
    {
      case 1:
        --v1;
        v12 -= 7i64;
        --v11;
        break;
      case 2:
        ++v1;
        v12 += 7i64;
        ++v11;
        break;
      case 3:
        --v2;
        --v8;
        --v10;
        break;
      default:
        if ( v21[v9] != 4 )
          exit(0);
        ++v2;
        ++v8;
        ++v10;
        break;
    }
    if ( *(_DWORD *)&asc_140003350[4 * (v12 + v8)] == 1 )
    {
      sub_140001020("You lost", v10, v11);
      exit(0);
    }
    if ( v11 > 6 || v10 > 6 )
    {
      puts("illegal access");
      exit(0);
    }
    ++v9;
  }
  while ( v9 < 26 );
  if ( *(_DWORD *)&asc_140003350[4 * (v2 + 7i64 * v1)] != 99 )
    _exit(0);
  puts("You win!");
```

其中`asc_140003350`是一个DWORD数组，这份代码可以透露出这个数组长度为49。大致可以判断为迷宫题，根据这个switch判断迷宫尺寸为7x7

查看`asc_140003350`得到该数组：

```python
arr = [8, 1, 14, 11, 7, 16, 1, 11, 15, 15, 1, 1, 9, 1, 1, 1, 1, 1, 1, 11, 1, 12, 12, 8, 14, 1, 8, 1, 8, 1, 1, 12, 9, 14, 1, 13, 8, 11, 1, 1, 1, 1, 1, 1, 9, 10, 9, 9, 99]
#len(arr) == 49
```

最后一个元素就是迷宫的终点。

稍微处理下

```python
for i in range(7):
    for j in range(7):
        tmp = 'O' if arr[i*7 + j] != 1 else 'X'
        print(tmp, end='')
    print()
```

输出：

```
#output:
OXOOOOX
OOOXXOX
XXXXXOX
OOOOXOX
OXXOOOX
OOOXXXX
XXOOOOO
```

根据`sub_1400010E0()`后面的部分

```c
do
{
    switch (v21[v0])
    {
    case 1:
        v15 = 82; //R
        break;
    case 2:
        v15 = 35; //#
        break;
    case 3:
        v15 = 90; //Z
        break;
    case 4:
        v15 = 70; //F
        break;
    default:
        goto LABEL_37;
    }
    putchar(v15);
LABEL_37:
    ++v0;
}
```

自行根据迷宫得到flag

`flag{#FFRFFF####ZZRZZZ##FF#FFFF}`
