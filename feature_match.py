import cv2
import numpy as np

cv2.namedWindow("img")
cap = cv2.VideoCapture(0)

detector = cv2.AKAZE_create()

while True:
    ret, img = cap.read()
    
    frameSize = img.shape
    half = cv2.resize(img, (img.shape[0]/2, img.shape[1]/2))
    flip = cv2.flip(half, 0)
    
    keypoint1, descript1 = detector.detectAndCompute(half, None)
    keypoint2, descript2 = detector.detectAndCompute(flip, None)
    
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck = True)
    matches = bf.match(descript1, descript2)
    
    matches = sorted(matches, key = lambda x:x.distance)
    
    dst = cv2.drawMatches(half, keypoint1, flip, keypoint2, matches, img, flags = 2)
    
    cv2.imshow("img", dst)
    
    if cv2.waitKey(1) == ord("q"):
        break
        
cv2.destroyAllWindows()
cap.release()