import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
img=cv.imread('C:\\Users\\gkred\\OneDrive\\Pictures\\Saved Pictures\\sample.jpg')
cv.imshow("Image",img)


blank=np.zeros(img.shape[:2],dtype='uint8')
cv.imshow("blank",blank)

mask=cv.circle(blank,(img.shape[1]//2+25,img.shape[0]//2),320,255,-1)
cv.imshow('mask',mask)

masked=cv.bitwise_and(img,img,mask=mask)
cv.imshow("masked image",masked)
cv.waitKey(0)
