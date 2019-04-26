# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 14:37:37 2019

@author: Sunny
张某人ER https://blog.csdn.net/xinxing__8185/article/details/48440133 
"""

import cv2
#import time
vc = cv2.VideoCapture('D:/pic0424/IMG_6101.MOV') #读入视频文件
#vidcap = cv2.VideoCapture(1)
c=0

if vc.isOpened(): #判断是否正常打开
    rval , frame = vc.read()
#    cv2.imshow("capture", frame)
#    time.sleep(3)
#    cv2.imwrite('D:/pic0424/' + 'sc' + str(c) + '.jpg',frame)
else:
    rval = False

timeF = 10  #视频帧计数间隔频率

while rval:   #循环读取视频帧
    rval, frame = vc.read()
    if(c%timeF == 0): #每隔timeF帧进行存储操作
        cv2.imwrite('D:/pic0424/brown/' + 'w_' + str(c) + '.jpg',frame) #存储为图像
    c = c + 1
    cv2.waitKey(1)
vc.release()
