import cv2 as cv
import numpy as np

img=cv.imread('C:\\Users\\gkred\\OneDrive\\Pictures\\Saved Pictures\\sample.jpg')
#cv.imshow(" ",img)

blank=np.zeros((500,500,3),dtype='uint8')

# Change the color of the right half to white
blank[200:300,300:400] =0, 255,0 
#cv.imshow('Blank',blank)

#cv.rectangle(blank,(0,0),(250,250),color=(34,47,187),thickness=cv.FILLED)

cv.rectangle(blank,(0,0),(img.shape[1]//2,img.shape[0]//2),color=(34,47,187),thickness=cv.FILLED)

#cv.imshow('Rectangle',blank)

cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),100,color=(20,50,35),thickness=-1)
#cv.imshow('Blank',blank)    

cv.line(blank,(34,56),(77,245),(23,11,89),thickness=3)

#cv.imshow(" ",blank)

cv.putText(blank,'Dont stare at me please',(200,255),cv.FONT_HERSHEY_TRIPLEX,fontScale=1.0,color=(0,255,0),thickness=2)
cv.imshow("",blank)
cv.waitKey(0)