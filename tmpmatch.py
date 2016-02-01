import cv2
import numpy as np

src = cv2.imread("cat.jpeg")
tmp = np.empty((50,50,3), dtype = np.uint8)

srcH, srcW, srcD = src.shape
tmpH, tmpW, tmpD = tmp.shape

tmp[:,:,:] = src[(srcH-tmpH)/2:(srcH+tmpH)/2, (srcW-tmpW)/2:(srcW+tmpW)/2, :]

res = cv2.matchTemplate(src, tmp, cv2.TM_CCOEFF_NORMED)

(minval, maxval, minloc, maxloc) = cv2.minMaxLoc(res)

rect1 = (maxloc[0], maxloc[1])
rect2 = (maxloc[0] + tmpW, maxloc[1] + tmpH)
cv2.rectangle(src, rect1, rect2, 0x00ff00)

cv2.imshow("src", src)
cv2.imshow("tmp", tmp)
cv2.waitKey(0)
cv2.destroyAllWindows()