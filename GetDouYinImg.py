import os
import time

from PIL import Image

# 图片压缩比例
SIZE_normal = 1.0
SIZE_small = 1.5
SIZE_more_small = 2.0


'''
adb手机截图
'''


def get_dou_yin_img():
    # 截图
    os.system("adb shell /system/bin/screencap -p /sdcard/screenshot.jpg")
    os.system("adb pull /sdcard/screenshot.jpg face.jpg")
    # 压缩图片
    img = Image.open("face.jpg").convert('RGB')
    scale = SIZE_small
    w, h = img.size
    img.thumbnail((int(w / scale), int(h / scale)))
    img.save('face.jpg')


'''
点小爱心
'''


def click_like():
    time.sleep(0.2)
    # os.system("adb shell input tap x y") 点赞心形的坐标
    # 适用于1280x720
    os.system("adb shell input tap 650 650")
    # os.system("adb shell input tap 1076 1078") # 点击事件，一加3
    # os.system("adb shell input tap 1476 1394")  # 点击事件，小米平板2


'''
下滑新的视频
'''


def switch_video():
    # os.system("adb shell input swipe 540 1300 540 500 100")
    # 适用于1280x720
    os.system('adb shell input swipe 540 700 540 100 100')
