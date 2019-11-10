# Android WP Sign_in

解压apk，用`jad classes.dex`得到`classes-dex2jar.jar`，再用`jd-gui`反编译得到java文件，在MainActivity.class看到

```java
public void onClick(View paramView) {
    if (paramView.getId() == 2131165218) {
      if (Base64.encodeToString(this.ed.getText().toString().getBytes(), 2).equals(getResources().getString(2131427369))) {
        this.tv.setText("Right");
        Toast.makeText(this, "Right", 1).show();
        return;
      } 
      this.tv.setText("Try again");
      Toast.makeText(this, "False", 1).show();
    } 
  }
```

第三行的比较就是题目关键了，`getString()`的数字是用来比较的base64编码后的字符串id，在反编译后的R.class找到

![1570926628470.png](https://i.loli.net/2019/10/16/kIgVR5aBubnQsED.png)

在`resources.arsc`查找sign找到这个：

![1570927250373.png](https://i.loli.net/2019/10/16/ZDVArCnFk52JfHa.png)

base64解码一下得到flag：

```python
>>> from base64 import b64decode
>>> b64decode("U3lje1NpOW5fMW5fSTNfRTRzeSF9")
b'Syc{Si9n_1n_I3_E4sy!}'
```
