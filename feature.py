import cv2
import numpy as np

cv2.namedWindow("dst1")
cv2.namedWindow("cont")
cap = cv2.VideoCapture(1)

detector = cv2.AKAZE_create()
a = 10
lut = np.array([(255.0/(1+np.exp(-a*(i-128.0)/255.0))) for i in range(256)],
                    dtype = np.uint8)
while True:
    ret, img = cap.read()
    cont = cv2.LUT(img, lut)
    keypoints = detector.detect(img)
    print "img:",len(keypoints),
    dst1 = cv2.drawKeypoints(img, keypoints, None)
    keypoints = detector.detect(cont)
    print"cont:",len(keypoints)
    dst2 = cv2.drawKeypoints(cont, keypoints, None)
    
    cv2.imshow("dst1", dst1)
    cv2.imshow("cont", dst2)    
    ch = cv2.waitKey(1)
    if ch == ord("q"):
        break
cv2.destroyAllWindows()
cap.release()