import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
img=cv.imread('C:\\Users\\gkred\\OneDrive\\Pictures\\Saved Pictures\\sampleee.png')
cv.imshow("Image",img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

threshold,thresh=cv.threshold(gray,125,255,cv.THRESH_BINARY)
cv.imshow('Simple Thresholded',thresh)

threshold,thresh_inv=cv.threshold(gray,105,255,cv.THRESH_BINARY_INV)
cv.imshow('Simple Thresholdedinverse',thresh_inv)

adaptive_thresh=cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,11,50)
cv.imshow('adaptive thresh',adaptive_thresh)

cv.waitKey(0)