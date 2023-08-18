import cv2 as cv
img=cv.imread('C:\\Users\\gkred\\OneDrive\\Pictures\\Saved Pictures\\sample.jpg')
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

blur=cv.GaussianBlur(img,(11,11),cv.BORDER_DEFAULT)
cv.imshow("Blur",blur) 

canny=cv.Canny(blur,125,175)
cv.imshow("canny",canny)

dilated=cv.dilate(canny,(3,3),iterations=1)
cv.imshow(" ",dilated)

eroded=cv.erode(dilated,(3,3),iterations=1)
cv.imshow('Eroded',eroded)

resized= cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
cv.imshow('Resized',resized)

cropped=img[50:200,200:490]
cv.imshow("Cropped",cropped)




cv.waitKey(0)