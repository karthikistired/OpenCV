import cv2 as cv
import numpy as np
img=cv.imread('C:\\Users\\gkred\\OneDrive\\Pictures\\Saved Pictures\\sampleee.png')
cv.imshow("Image",img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

blur=cv.GaussianBlur(gray,(5,5),cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)
blank=np.zeros(img.shape,dtype='uint8')
#cv.imshow('Blank',blank)

canny=cv.Canny(blur,0,25)
cv.imshow('Canny edges',canny)

ret,thresh=cv.threshold(gray,140,200,cv.THRESH_BINARY)
cv.imshow("thresh",thresh)



contours,heirarchies=cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)

print(len(contours))

cv.drawContours(blank,contours,-1,(0,0,255),2)
cv.imshow("contours",blank)


cv.waitKey(0)

