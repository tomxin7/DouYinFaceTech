<p align="center">
<img src="https://github.com/tomxin7/DouYinFaceTech/blob/master/banner.png?raw=true" alt="Material Render Phone">
</p>

<h1 align="center"><a href="http://tomxin.cn" target="_blank">Tomxin7 </a></h1>

> Simple, Interesting | 简单，有趣


## 什么是抖音

> 抖音是2016年9月上线的一款音乐创意短视频社交软件，是一个专注年轻人的15秒音乐短视频社区。用户可以通过这款软件选择歌曲，拍摄15秒的音乐短视频，形成自己的作品。


![](/20180418_000727.gif)

## 需求
抖音经常能刷到很多高质量的视频，特别是我们使用的越多，头条的算法给我们推荐的内容越精准。**那么我们可不可以写一个小型的程序，根据自己设置的特征筛选视频并且自动点赞存入我们的收藏夹中呢？比如漂亮的小姐姐，帅气的小哥哥或者是可爱的喵星人。。。**

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

5. 如果满足要求，使用ADB点击屏幕

6. 上滑切换新视频 





## 使用教程

相关软件工具安装和使用步骤请参考 [Android 和 iOS 操作步骤](https://github.com/wangshub/wechat_jump_game/wiki/Android-%E5%92%8C-iOS-%E6%93%8D%E4%BD%9C%E6%AD%A5%E9%AA%A4)

#### 获取源码

```
- git clone https://github.com/wangshub/wechat_jump_game.git

```
##### 非常推荐使用Python3，避免编码及i

## 版本说明

- master 分支：稳定版本，已通过测试

