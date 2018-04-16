from GetFaceInfo import *
from GetDouYinImg import *


if __name__ == '__main__':
    token="24.0157b70757727316d7f56f5eb8c1bfbe.2592000.1526359908.282335-11097784"
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