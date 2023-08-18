import numpy as np
import cv2 as cv

haar_cascade=cv.CascadeClassifier('D:\\AI\\ML\\CV\\haar_face.xml')

people=['amrutha']
""" features=np.load('features.npy')
labels=np.load('labels.npy') """

face_recognizer=cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')

img=cv.imread("C:\\Users\\gkred\\OneDrive\\Pictures\\face_train\\val\\amrutha\\IMG_20230425_191645_917.jpeg")

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

cv.imshow('Person',gray)

faces_rect=haar_cascade.detectMultiScale(gray,1.1,4)

for(x,y,w,h) in faces_rect:
    faces_roi=gray[y:y+h,x:x+h]

    label,confidence=face_recognizer.predict(faces_roi)
    print(f'Label = {people[label]} with a confidence of {confidence}')

    cv.putText(img,"Hey amrutha! You have a pretty smile :)",(150,100),cv.FONT_HERSHEY_COMPLEX,1.0,(147,20,255),thickness=4)

    cv.rectangle(img,(x,y),(x+w,y+h),(147,30,255),thickness=2)
cv.imshow('Detected Face',img)

cv.waitKey(0)