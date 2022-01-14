# useful-tools

Organize and collect some useful daily tools

所有工具脚本均在`python3.8.2`下测试运行，安装依赖环境`pip install -r requirement.txt`

#### [jets_code](https://github.com/stellae216/useful-tools/blob/main/jets_code/jets_code.py) - 下载jetbrains激活码

激活码有效期比较短，过期需要重新下载。运行需要添加激活码地址参数。

示例:

```python
python jets_code.py --url http://idea.medeming.com/jets/images/jihuoma.zip
```

```text
激活码地址:
http://idea.medeming.com/jets/images/jihuoma.zip

Pycharm/Goland:
http://idea.medeming.com/a/jihuoma2.zip

Webstorm:
http://idea.medeming.com/a/jihuoma3.zip

IDEA:
https://idea.medeming.com/a/jihuoma.zip
```

#### [breakvip](https://github.com/stellae216/useful-tools/blob/main/breakvip/breakvip_movies.py)  - 解析[布雷克影院](http://www.breakvip.com/)电影资源并下载到本地

将需要付费的web播放地址作为参数传入运行，如：`--address http://www.breakvip.com/v_play/xxxxx.html`

> 下载资源为`.ts`格式，使用 `QuickTime Player` 或 `PotPlayer` 播放

#### [mysecret](https://github.com/stellae216/useful-tools/blob/main/mysecret/mysecret.py)

随机生成指定长度伪随机密码

#### [getseal](https://github.com/stellae216/useful-tools/blob/main/getseal/getseal.py) - 扣取印章

运行程序: `python getseal.py -i source.png -o out.png`
