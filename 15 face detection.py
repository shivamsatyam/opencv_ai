import cv2 as cv

img = cv.imread('Photos/group 1.jpg')
cv.imshow('img',img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

haar_cascade = cv.CascadeClassifier('har_face.xml')
faces_rect = haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=1)




print(len(faces_rect))

for (x,y,w,h) in faces_rect:
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=2)
cv.imshow('img',img)

cv.waitKey(0)









# import cv2 as cv

# haar_cascade = cv.CascadeClassifier('har_face.xml')

# capture = cv.VideoCapture('b.mp4')
# while True:
#     isTrue,frame = capture.read() # read the video frame by frame and return a boolean for succesfylly captured
#     gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
#     faces_rect = haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=8)

#     for (x,y,w,h) in faces_rect:
#         cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),thickness=2)

#     cv.imshow('Video',frame)

#     if cv.waitKey(20) & 0xFF == ord('d'):
# 	    break

# capture.release()
# cv.destroyAllWindows()




# cv.waitKey()






































