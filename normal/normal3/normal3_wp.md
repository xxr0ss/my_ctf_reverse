本题主要难点是递归（断断续续做了很多次，终于做出来了）

```c++
__int64 __fastcall main(__int64 a1, char **a2, char **a3)
{
  __int64 result; // rax

  puts("Input flag:");
  __isoc99_scanf("%64s", &byte_601100);
  dword_601064 = 0;
  sub_400666(0LL);
  if ( !strcmp(&s1, "bcec8d7dcda25d91ed3e0b720cbb6cf202b09fedbc3e017774273ef5d5581794") )
  {
    memset(&s1, 0, 0x80uLL);
    dword_601064 = 0;
    sub_4006BE(0LL, 0LL);
    if ( !strcmp(&s1, "7d8dcdcaed592e1dcb07e02c36bcb2f0bf9e0bdcb0e13777237e25fd48515974") )
      printf("TQL! TQL! flag: nctf{%s}\n", &byte_601100);
    else
      puts("Emmmm.....");
    result = 0LL;
  }
  else
  {
    puts("GG!");
    result = 0LL;
  }
  return result;
}
```

其实只有`sub_400666()`要管，`sub_4006BE()`其实是重复校验了一遍，不用分析。

```c++
//sub_400666()
__int64 __fastcall sub_400666(signed int a1)
{
  int v1; // eax
  __int64 result; // rax

  if ( a1 <= 63 )
  {
    v1 = dword_601064++;
    *(&s1 + v1) = byte_601100[a1];
    sub_400666((unsigned int)(2 * a1 + 1));
    result = sub_400666((unsigned int)(2 * (a1 + 1)));
  }
  return result;
}
```

说明下，`dword_601064`是个全局变量，这个递归函数保证了`dword_601064`最后加到了63，得到包含64个字符的字符串s1：`"bcec8d7dcda25d91ed3e0b720cbb6cf202b09fedbc3e017774273ef5d5581794"`



这个递归其实没必要有返回值，难点在于确认s1每一个字符是输入的第几个字符，我的方法是：

```python
def s(a1):
    global cnt, nums
    if a1 <= 63:
        cnt += 1
        nums.append(a1)
        s(2*a1 + 1)
        s(2*(a1 + 1))
def main():
    global cnt, nums
    cnt = 0
    nums = []
    s(0)
    print(s)
```

得到`nums == [0, 1, 3, 7, 15, 31, 63, 32, 16, 33, 34, 8, 17, 35, 36, 18, 37, 38, 4, 9, 19, 39, 40, 20, 41, 42, 10, 21, 43, 44, 22, 45, 46, 2, 5, 11, 23, 
47, 48, 24, 49, 50, 12, 25, 51, 52, 26, 53, 54, 6, 13, 27, 55, 56, 28, 57, 58, 14, 29, 59, 60, 30, 61, 62]` (可以确认`len(nums) == 64`)

就是说：

 * s1[0] = input[0]

 * s1[1] = input[1]

 * s1[2] = input[3]

 * s1[3] = input[7]

   .......

所以用：

```python
flag = [0 for i in range(64)]
    for i in range(64):
        flag[nums[i]] = s1[i]
    print(''.join(flag))
```

得到flag:

`nctf{c2e3b4c2eb03258c5102bf9de77f57dddad9edb70c6c20febc01773e5d81947}`