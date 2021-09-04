import cv2 as cv
import numpy as np

img = cv.imread('Photos/cats.jpg')
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)


"""laplacian"""

lap = cv.Laplacian(gray,cv.CV_64F) # src,ddepth,dst=None,ksize=None,scale=None,delta=None,borderType=None
# print(lap)
lap = np.uint8(np.absolute(lap))
cv.imshow('lapsian',lap)


"""sobel"""
sobelX = cv.Sobel(gray,cv.CV_64F,1,0)
sobelY = cv.Sobel(gray,cv.CV_64F,0,1)
cv.imshow('sobelX',sobelX)
cv.imshow('sobelY',sobelY)



cv.waitKey(0)
















































