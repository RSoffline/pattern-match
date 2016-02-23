import cv2
import numpy as np

img = cv2.imread("cat.jpeg")

#detector = cv2.FastFeatureDetector_create()
detector = cv2.ORB_create()
keypoints = detector.detect(img)
dst = cv2.drawKeypoints(img, keypoints, None)

cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyWindow("dst")
