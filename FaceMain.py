from GetFaceInfo import *
from GetDouYinImg import *


if __name__ == '__main__':

    # client_id 为官网获取的AK， client_secret 为官网获取的SK
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=【官网获取的AK】&client_secret=【官网获取的SK】'
    token = get_token(host)
    i = 1
    while(1):
        print("------------------第" + str(i) + "个视频------------------")
        # 获取抖音的截图
        getDouYinImg()
        #调用百度人脸识别API
        face_dict = getBaiDuFaceTech("face.jpg",token )
        #得到的数据进行分析
        faceInfoAnalysis(face_dict)
        i+=1