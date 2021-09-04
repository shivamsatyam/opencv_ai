import cv2 as cv
import numpy as np



img = cv.imread('Photos/cats.jpg')
# cv.imshow('image',img)

blank = np.zeros(img.shape,dtype='uint8')


gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow('gray',gray)

# blur = cv.GaussianBlur(img,(5,5),cv.BORDER_DEFAULT)

# canny = cv.Canny(blur,125,175)
# cv.imshow('canny',canny)



#cv.RETR_LIST  list of the contours
#cv.RETR_EXTERNAL only external countours
#cv.RETR_TREE all hierachal contours

# cv.CHAIN_APPROX_NONE

ret,thresh = cv.threshold(gray,125,225,cv.THRESH_BINARY)
cv.imshow('thresh',thresh)


contours,hierachies = cv.findContours(thresh,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE) #imgae,mode,method,contours=none,hierachy=None,offset=None
print(len(contours))



"""drawing contours"""
cv.drawContours(blank,contours,-1,(0,0,255),1) # image,contours,contourIDs=> for showing all the contours set to -1,color,thickness
cv.imshow('drawContours',blank)


cv.waitKey(0)






































