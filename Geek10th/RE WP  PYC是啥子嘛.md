# RE WP  PYC是啥子嘛? 

本题目是pyc文件的逆向

需要使用工具`uncompyle`，安装方法推荐使用pip安装：

```shell
pip install uncompyle
```

解题过程：

```
uncompyle6 re_py.pyc
```

得到逆向后的python2代码：

```python
print 'This is a maze.'
print 'Python is so easy.'
print 'Plz Input The Shortest Way:'
maze = '###########S#@@@@@@##@#@####@##@#@@@@#@##@####@#@##@@@@@@#@#########@##E######@##@@@@@@@@###########'
way = raw_input()
len = len(way)
p = 11
for i in way:
    if i == '&':
        p -= 10
    if i == '$':
        p += 10
    if i == '6':
        p -= 1
    if i == '3':
        p += 1
    if maze[p] == '#':
        print 'Your way is wrong'
        exit(0)
        break
    if maze[p] == '@':
        continue
    if maze[p] == 'E':
        print 'You do it,your flag is Syc\\{+Your Input+\\}.'
        exit(0)

print 'May be something wrong.'
```

题目还是不是很难，我的解题步骤如下：

注意到len(maze) == 100，猜测maze尺寸是10 * 10，输出得到

```python
>>>for i in range(10):
   print(maze[i * 10: i * 10 + 10])

##########
#S#@@@@@@#
#@#@####@#
#@#@@@@#@#
#@####@#@#
#@@@@@@#@#
########@#
#E######@#
#@@@@@@@@#
##########
```

根据逆向的python代码判断上下左右为&$63

得到正确路线：`$$$$33333&&666&&33333$$$$$$$6666666&`

所以flag:`Syc{$$$$33333&&666&&33333$$$$$$$6666666&}`

