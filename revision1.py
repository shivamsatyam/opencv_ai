import os
import cv2 as cv
import numpy as np

people = ['Mindy Kaling','shivam']

DIR = r'E:\hangman\clock\opencv\train'
p  = []
haar_cascade = cv.CascadeClassifier('har_face.xml')
# features = np.load('features.npy',allow_pickle=True)
# labels = np.load('labels.npy',allow_pickle=True)


face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')

img = cv.imread(r'E:\hangman\clock\opencv\train\shivam\IMG_20210509_220620.jpg')
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

cv.imshow('img',gray)

faces_rect = haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=4)


for (x,y,w,h) in faces_rect:
    faces_roi = gray[y:y+h,x:x+w]
    label,confidence = face_recognizer.predict(faces_roi)    
    print(confidence)
    print(label)
    cv.putText(img,str(people[int(label)]),(20,20),cv.FONT_HERSHEY_COMPLEX,1.0,(0,255,0),thickness=2)
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=2)
cv.imshow('face',img)

cv.waitKey(0)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
