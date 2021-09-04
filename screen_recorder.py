import cv2 as cv
from PIL import ImageGrab
import numpy as np
from win32api import GetSystemMetrics

width = GetSystemMetrics(0)
height = GetSystemMetrics(1)

fourcc = cv.VideoWriter_fourcc('m','p',"4","v")
captured_video = cv.VideoWriter('output.mp4',fourcc,20.0,(width,height))

while True:
    image = np.array(ImageGrab.grab(bbox=(0,0,width,height)))
    image = cv.cvtColor(image,cv.COLOR_BGR2RGB)
    
    # cv.imshow('image',image)    
    
    captured_video.write(image)    
        
    
    if cv.waitKey(10)==ord('q'):
        break

































