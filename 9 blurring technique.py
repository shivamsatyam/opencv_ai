import cv2 as cv


img = cv.imread('Photos/cats.jpg')
cv.imshow('img',img)

"""Averaging"""
# average = cv.blur(img,(7,7)) # src,ksize,dst=None,anchor=None borderType=None
# cv.imshow('average',average)

"""GaussinaBlur"""
# gauss = cv.GaussianBlur(img,(3,3),0)
# cv.imshow('gauss',gauss)

"""medianBlur"""

# median = cv.medianBlur(img,3)
# cv.imshow('median',median)

"""Bilateral"""
# bilateral = cv.bilateralFilter(img,5,15,15) #src,diameter,sigmaColor,sigmaSpace
# cv.imshow('bilateral',bilateral)



cv.waitKey(0)






































