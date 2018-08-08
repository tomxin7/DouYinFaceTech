<p align="center">
<img src="https://github.com/tomxin7/DouYinFaceTech/blob/master/banner1.png?raw=true" alt="Material Render Phone">
</p>

<h1 align="center"><a href="http://tomxin.cn" target="_blank">Tomxin7 </a></h1>

> Simple, Interesting | 简单，有趣

## 什么是抖音

> 抖音是2016年9月上线的一款音乐创意短视频社交软件，是一个专注年轻人的15秒音乐短视频社区。用户可以通过这款软件选择歌曲，拍摄15秒的音乐短视频，形成自己的作品。


## 效果
抖音经常能刷到很多高质量的视频，特别是我们使用的越多，头条的算法给我们推荐的内容越精准。**那么我们可不可以写一个小型的程序，根据自己设置的特征筛选视频并且自动点赞存入我们的收藏夹中呢？比如漂亮的小姐姐，帅气的小哥哥或者是可爱的喵星人。。。**
<!--more-->


![](https://github.com/tomxin7/DouYinFaceTech/raw/master/20180418_000727.gif)
## 原理说明

##### 本程序与抖音无关，主要供学习用途

1. 将手机打开抖音的推荐视频界面

2. 用 ADB 工具获取当前手机截图，并用 ADB 将截图 pull 上来
```shell
adb shell screencap -p /sdcard/autojump.png
adb pull /sdcard/autojump.png .
```

3. 将图片进行压缩,并调用[百度人脸识别API](http://ai.baidu.com/tech/face)


4. 获得百度返回的数据进行判断分析

5. 如果满足要求，使用ADB点赞

6. 上滑切换新视频 





## 使用教程


#### 1、获取源码
github地址
```
https://github.com/tomxin7/DouYinFaceTech
```
git命令
```
git clone https://github.com/tomxin7/DouYinFaceTech.git
```
#### 2、依赖
```
Python：3.6.1 
ADB下载：http://adbshell.com/downloads
```
#### 3、准备
```
使用数据线连接手机与电脑，并开启调试模式
启动ADB，保证驱动安装（保证可以连接360手机助手等软件）
FaceMain.py中替换token的host链接
```
#### 4、运行
```
手机打开抖音，PC退出手机助手等软件
DouYinFaceTech目录下直接运行FaceMain.py
```
