# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 15:18:54 2016

@author: ryusei
"""

import cv2
import numpy as np
import sys
import traceback


def TemplateMatch(src, tmp):
    res = cv2.matchTemplate(src, tmp, cv2.TM_CCOEFF_NORMED)
    (minval, maxval, minloc, maxloc) = cv2.minMaxLoc(res)
    rect1 = (maxloc[0], maxloc[1])
    rect2 = (maxloc[0] + tmp.shape[1], maxloc[1] + tmp.shape[0])
    cv2.rectangle(src, rect1, rect2, 0x00ff00)
    
cam = [cv2.VideoCapture(i) for i in range(1,3)]
tmpSize = (100L, 100L, 3L)

try:
    while True:
        frame = {i:cam[i].read() for i in range(2)}
        if not frame[0] or not frame[1]:
            print "no cam"            
            break
        frameSize = frame[0][1].shape
        tmp = np.empty(tmpSize, dtype = np.uint8)
        
        tmp[:, :, :] = frame[0][1][(frameSize[0] - tmpSize[0])/2:(frameSize[0] + tmpSize[0])/2,
                                   (frameSize[1] - tmpSize[1])/2:(frameSize[1] + tmpSize[1])/2,
                                   :]
        TemplateMatch(frame[1][1], tmp)
        cv2.rectangle(frame[0][1], ((frameSize[1] - tmpSize[1])/2, (frameSize[0] - tmpSize[0])/2),
                                   ((frameSize[1] + tmpSize[1])/2, (frameSize[0] + tmpSize[0])/2),0x00ff00)
        for i in frame:
            cv2.imshow(str(i), frame[i][1])
        cv2.imshow("tmp", tmp)
        if cv2.waitKey(1) & 0xff == ord("q"):
            print "break"
            break
except:
    print "-" * 20
    print traceback.format_exc(sys.exc_info()[2])
    print "-" * 20

finally:
    for i in cam:
        i.release()
    cv2.destroyAllWindows()
    