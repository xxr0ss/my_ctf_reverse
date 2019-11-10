# Android WP  蒋学姐的秘密

JEB是个好东西，先把apk丢JEB里面，在`LoginActivity.class`反编译代码中分析一下应用的逻辑。

手机上的界面比较简洁，就是一个登录界面，来看反编译`LoginActivity`的部分：

`onCreate()`：

```java
PackageInfo v3_2;

//...

PackageManager v3 = this.getPackageManager();
try {
    v3_2 = v3.getPackageInfo(this.getPackageName(), 0);
}

//...
v3_2 = v3.getPackageInfo(this.getPackageName(), 0); //v3_2 == 'Syclover',就是用户名
```
`onCreate`比较靠下面的地方

```java
public void onClick(View arg3) {
    this.val$loadingProgressBar.setVisibility(0);
    LoginActivity.this.loginViewModel.login(this.val$usernameEditText.getText().toString(), this.val$passwordEditText.getText().toString());
}
```

把输入的username和password传入`login()`，一路跟进

`loginViewModel --> loginRepository --> dataSource`最终在`LoginDataSource.class`看到账号密码校验过程：

```java
public Result login(String username, String password) {
    try {
        if(username.equals(LoginActivity.VersionName)) {
            //判断用户名是不是LoginActivity.VersionName
            StringBuilder v0 = new StringBuilder();
            v0.append("Syc{");
            v0.append(LoginDataSource.login(username));
            v0.append("}");
            if(password.equals(v0.toString())) {
                return new Success(new LoggedInUser(UUID.randomUUID().toString(), username));
            }

            return new Error(new Exception("wrong password"));
        }

        return new Error(new Exception("wrong user"));
    }
    catch(Exception v3) {
        return new Error(new IOException("Error logging in", ((Throwable)v3)));
    }
}
```

其中`Line 6`调用的就是个标准的md5加密：

```java
public static String login(String arg4) {
    try {
        MessageDigest v0 = MessageDigest.getInstance("MD5");
        v0.update(arg4.getBytes());
        StringBuffer v4_1 = new StringBuffer();
        byte[] digest = v0.digest();
        int i;
        for(i = 0; i < digest.length; ++i) {
            int v2 = digest[i];
            if(v2 < 0) {
                v2 += 0x100;
            }

            if(v2 < 16) {
                v4_1.append("0");
            }

            v4_1.append(Integer.toHexString(v2));
        }

        return v4_1.toString();
    }
    catch(NoSuchAlgorithmException v4) {
        v4.printStackTrace();
        return "";
    }
}
```

---

到此程序的逻辑出来了，先获取`LoginActivity.VersionName`，将username进行比较，然后将其计算md5得到哈希值 `8ed847f4164c5b6e87fa2508a05181d1`，密码即是Syc{哈希值}

得到flag：

`Syclover{8ed847f4164c5b6e87fa2508a05181d1}`