# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 15:55:55 2019

@author: Sunny
"""

#import cv2

# Windows dependencies
# - Python 2.7.6: http://www.python.org/download/
# - OpenCV: http://opencv.org/
# - Numpy -- get numpy from here because the official builds don't support x64:
#   http://www.lfd.uci.edu/~gohlke/pythonlibs/#numpy

# Mac Dependencies
# - brew install python
# - pip install numpy
# - brew tap homebrew/science
# - brew install opencv
'''
import cv2
import time
cap = cv2.VideoCapture(0)
#time.sleep(2)
ret, frame = cap.read()
#rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
#cv2.imwrite('D:/egg0711/capture.jpg', frame)
#cap.release()
#ticks = time.time()
#print (time.strftime("%y%m%d_%H%M%S" , time.localtime()))

while(True):
    ret, frame = cap.read()
#    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        out = cv2.imwrite('D:/egg0711/capture.jpg', frame)
        break

cap.release()
cv2.destroyAllWindows()
'''

import cv2

cv2.namedWindow("preview")
vc = cv2.VideoCapture(1)
x_mid=320
y_mid=240
if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False

while rval:
    cv2.imshow("preview", frame)
    rval, frame = vc.read()
    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break
    elif key==32:
        cv2.imwrite('D:/SC/tt/capture.jpg', frame)
        print('capture')
        continue
    else:
#        cv2.line(img=frame, pt1=(50, 10), pt2=(150, 10), color=(255, 0, 0), thickness=8, lineType=8, shift=0)
        # big
        cv2.rectangle(frame, (int(x_mid*0.3), int(y_mid*0.03)), (int(x_mid*1.72), int(y_mid*1.94)), (0, 255, 0), 2)
#        cv2.circle(frame,(320, 240), 10, (0, 0, 255), 3)
        # small
        cv2.rectangle(frame, (int(x_mid*0.48), int(y_mid*0.245)), (int(x_mid*1.51), int(y_mid*1.73)), (0, 255, 0), 2)
        cv2.circle(frame,(320, 240), 10, (0, 0, 255), 2)
        cv2.circle(frame,(320, 350), 10, (0, 150, 255), 2)
vc.release()
cv2.destroyWindow("preview")   



