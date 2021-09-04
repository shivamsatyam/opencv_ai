import cv2 as cv

img = cv.imread('Photos/cats.jpg')

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)



""""simple threshhold"""

threshold,thresh = cv.threshold(gray,150,255,cv.THRESH_BINARY) # src,thresh=> pixel intensity greater tham,maxval,type,dst=None
cv.imshow('threshold',thresh)

thresholdinv,threshinv = cv.threshold(gray,150,255,cv.THRESH_BINARY_INV) # src,thresh=> pixel intensity greater tham,maxval,type,dst=None
cv.imshow('thresholdinv',threshinv)

"""Adatiuve threshhold"""

adaptive_thresh = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,3) # src,maxValue,adatuveMethod,threshholdType,blocksize,c
cv.imshow('adaptiveThreshold',adaptive_thresh)



cv.waitKey(0)






















































