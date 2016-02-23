import cv2
import numpy as np

src = cv2.imread("cat.jpeg")
cv2.namedWindow("dst2")
cap = cv2.VideoCapture(0)
#detector = cv2.FastFeatureDetector_create()

detector = cv2.ORB_create()
keypoints = detector.detect(src)
dst = cv2.drawKeypoints(src, keypoints, None)
cv2.imshow("dst", dst)

while True:
    ret, img = cap.read()
    keypoints = detector.detect(img)
    dst = cv2.drawKeypoints(img, keypoints, None)
    cv2.imshow("dst2", dst)
    #cv2.imshow("dst", dst)
    ch = cv2.waitKey(1)
    if ch == ord("q"):
        break
cv2.destroyAllWindow()
