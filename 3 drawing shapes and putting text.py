import cv2 as cv
import numpy as np


blank = np.zeros((500,500,3),dtype="uint8") 

"""changing the color of blank image"""
#blank[:] = 123,255,24



"""changing the color for a certain place"""

#blank[200:400,100:200] = 0,123,234

"""drawing a rectangle"""
# cv.rectangle(blank,(0,0),(200,400),(123,123,212),thickness=2) #img pt1,pt2,color,thickness,lineType
# cv.rectangle(blank,(0,0),(200,400),(123,123,212),thickness=cv.FILLED) #img pt1,pt2,color,thickness,lineType


"""draw a circle"""
# cv.circle(blank,(250,250),40,(0,123,231),thickness=3) # img centre radius color thickness lineType
# cv.circle(blank,(250,250),40,(0,123,231),thickness=cv.FILLED) # img centre radius color thickness lineType


"""drawing a line"""
# cv.line(blank,(100,200),(400,200),(123,231,212),thickness=4) #img,pt1,pt2,color,thickness,lineType


"""putting text"""


cv.putText(blank,"Shivam the great",(10,225),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,255,0),3) #img text org fontFace fontScale color thickness lineType bottonLeftOrigin

cv.imshow('black',blank)
cv.waitKey(0)


































