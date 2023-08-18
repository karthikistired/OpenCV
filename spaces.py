import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
img=cv.imread('C:\\Users\\gkred\\OneDrive\\Pictures\\Saved Pictures\\sampleee.png')
cv.imshow("Image",img)
plt.imshow(img)
plt.show()
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("gray",gray)

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow("hsv",hsv)

lab=cv.cvtColor(img,cv.COLOR_BGR2LAB)
"""cv.imshow("lab",lab) 

rgb=cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow('rgb',rgb)

plt.imshow(rgb)
plt.show() """

hsv_bgr=cv.cvtColor(hsv,cv.COLOR_HSV2BGR)
cv.imshow('HSV--> BGR',hsv_bgr)

lab_bgr=cv.cvtColor(lab,cv.COLOR_Lab2BGR)
cv.imshow('LAB-->BGR',lab_bgr)

cv.waitKey(0)
