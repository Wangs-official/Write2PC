![](https://s3.bmp.ovh/imgs/2024/10/02/51e960a34f1481bb.png)
# Write2PC
通过WebSocket，为码字大佬们提供最简单的手机电脑文字同步

## 安装

请确定您的电脑含有 **Python** 环境

若没有,请自行搜索如何安装 **Python**

请打开cmd/终端,输入指令:`pip3 install Flask Flask-SocketIO`

然后进入 **发行版** 页面,下载最新的 **pc.zip** 并解压,然后运行 **app.py**

## 使用

在启动后,会显示以下内容:

```
 * Serving Flask app 'app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:14150
 * Running on http://192.168.1.111:14150
Press CTRL+C to quit
```

### PC/iOS

PC可打开 **127.0.0.1:14150**

iOS等其他平台请打开 **192.168.xxx.xxx:14150**

**192.168.xxx.xxx** 具体的IP在控制台

### Android

请在 **发行版** 页面下载安卓APP,点击上方 **状态** 按钮即可打开连接页面

请在对话框中输入要连接的IP(具体IP在控制台,请使用192开头的IP),并点击 **连接**

## 注意

1. 仅作为互通连接使用,并不是一个成熟的编辑器
2. 请及时保存您的作品,退出软件后不保留
3. 没有连接提示
