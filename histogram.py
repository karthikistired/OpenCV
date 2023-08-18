import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
img=cv.imread('C:\\Users\\gkred\\OneDrive\\Pictures\\Saved Pictures\\sampleee.png')
cv.imshow("Image",img)

""" gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("gray",gray) """

blank=np.zeros(img.shape[:2],dtype='uint8')

circle=cv.circle(blank,(img.shape[1]//2,img.shape[0]//2),100,255,-1)

mask=cv.bitwise_and(img,img,mask=circle)
cv.imshow('Mask',mask)


""" gray_hist=cv.calcHist([gray],[0],mask,[256],[0,256])

plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show() """
plt.figure()
plt.title('colour Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')

colours=('b','g','r')

for i,col in enumerate(colours):
    hist=cv.calcHist([img],[i],None,[256],[0,256])
    plt.plot(hist,color=col)
    plt.xlim([0,256])
plt.show()

cv.waitKey(0)