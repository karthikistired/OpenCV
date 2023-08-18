import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
img=cv.imread('C:\\Users\\gkred\\OneDrive\\Pictures\\Saved Pictures\\sampleee.png')
cv.imshow("Image",img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

lap=cv.Laplacian(gray,cv.CV_64F)
lap=np.uint8(np.absolute(lap))
cv.imshow('Laplacian',lap)
sobelx=cv.Sobel(gray,cv.CV_64F,1,0)
sobely=cv.Sobel(gray,cv.CV_64F,0,1)
COMBINED_SOBEL=cv.bitwise_or(sobelx,sobely)

cv.imshow('combine',COMBINED_SOBEL)

cv.imshow("sobelx",sobelx)
cv.imshow('sobely',sobely)

canny=cv.Canny(gray,20,80)
cv.imshow('canny',canny)


cv.waitKey(0)
