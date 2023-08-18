import cv2 as cv
#img=cv.imread('C:\\Users\\gkred\\OneDrive\\Pictures\\Saved Pictures\\sample.jpg')

#cv.imshow('avatar',img)

def rescaleframe(frame,scale=0.25):
    print(frame.shape)
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimensions=(width,height)

    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

capture=cv.VideoCapture('C:\\Users\\gkred\\Videos\\Captures\\sample.mp4')
while True:
    isTrue,frame=capture.read()
    frame_resized=rescaleframe(frame)
    cv.imshow('Video',frame)
    cv.imshow('Video resized',frame_resized)
    
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
    
capture.release()
cv.destroyAllWindows() 

