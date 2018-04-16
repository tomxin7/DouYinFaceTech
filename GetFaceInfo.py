# encoding:utf-8
import base64
import json
import urllib
import urllib.request
from urllib import request

import time

from GetDouYinImg import *


'''
进行post请求
url：请求地址
value：请求体
'''
def get_info_post_json_data(url,value):
    header_dict = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',"Content-Type": "application/json"}
    req = request.Request(url=url,data=value,headers=header_dict)
    res = request.urlopen(req)
    res = res.read()
    return (res.decode('utf-8'))

'''
调用百度API，进行人脸探测
imgPath：图片的地址
access_token：开发者token
'''
def getBaiDuFaceTech(imgPath,access_token):
    request_url = "https://aip.baidubce.com/rest/2.0/face/v1/detect"
    # 二进制方式打开图片文件
    f = open(imgPath, 'rb')
    # 图片转换为base64
    img = base64.b64encode(f.read())
    params = {"face_fields":"age,beauty,expression,faceshape,gender,glasses,landmark,race,qualities","image":img,"max_face_num":5}
    params=urllib.parse.urlencode(params).encode(encoding='utf-8')
    request_url = request_url + "?access_token=" + access_token
    #调用post请求方法
    face_info = get_info_post_json_data(request_url,params)
    #json字符串转对象
    face_json = json.loads(face_info)
    #如果没有发现人像，会返回空
    if face_json["result_num"]==0:
        face_dict={}
    else:
        #把想要的部分提取存入字典中
        result = face_json['result'][0]
        gender = result['gender']
        age = str(result['age'])
        race = str(result['race'])
        beauty = str(result['beauty'])
        face_dict = {"gender":gender,"age":age,"race":race,"beauty":beauty}
    return face_dict

'''
将获得的数据进行分析
face_dict：人脸识别后的数据
'''
def faceInfoAnalysis(face_dict):
    #如果发现人物继续判断
    if len(face_dict)!=0:
        #如果为女生继续判断
        if face_dict["gender"]=="female":
            print("性别：女")
            print("年龄："+face_dict["age"])
            print("颜值："+face_dict["beauty"])
            #如果颜值在40以上，并且年龄大于18继续
            if(float(face_dict["beauty"])>40 and float(face_dict["age"])>18):
                #点赞
                click_like()
                print("好可爱ヽ(✿ﾟ▽ﾟ)ノ 已喜欢❤")
                #点赞后休息一秒，主要为能够看到点击爱心的效果
                time.sleep(1)
            else:
                print("再看看(๑•̀ㅂ•́)و✧")
        else:
            print("没有发现小姐姐，下一个")
    else:
        print("没有发现小姐姐，下一个")
    #上滑新视频
    switch_video()
    # 上滑新视频之后给2s等待加载新视频
    time.sleep(2)
