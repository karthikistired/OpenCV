import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
img=cv.imread('C:\\Users\\gkred\\OneDrive\\Pictures\\Saved Pictures\\sample.jpg')
cv.imshow("Image",img)

average=cv.blur(img,(7,7))
cv.imshow('Average Blur',average)

""" gauss=cv.GaussianBlur(img,(7,7),0)
cv.imshow('Gaussian BLur',gauss)

med=cv.medianBlur(img,7)
cv.imshow("median",med) """

lateral=cv.bilateralFilter(img,100,95,605)
cv.imshow("bilateral",lateral)
cv.waitKey(0)
