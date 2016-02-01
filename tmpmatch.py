import cv2
import numpy as np

src = cv2.imread("test.jpg")
tmp = np.empty((50,50,3), dtype = np.uint8)

h, w, d = src.shape

tmp[:,:,:] = src[(h-50)/2:(h+50/2), (w-50)/2:(w+50/2), :]

