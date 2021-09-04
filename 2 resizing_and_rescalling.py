import cv2 as cv

#height and vidth

def rescaleFrame(frame,scale=0.75):
	width = int(frame.shape[1] + scale)
	height = int(frame.shape[0] + scale)

	dimension = (width,height)

	return cv.resize(frame,dimension,interpolation=cv.INTER_AREA)


"""changing resolution"""

def changeRes(width,height):
    """only work for live videos like webcam"""
    capture.set(3,width) # 3 stand for width property and 4 stand for height property
    capture.set(4,height)

# img = cv.imread('Photos/cat.jpg')
# cv.imshow('original',img)


# resize = rescaleFrame(img,100)
# cv.imshow('resize',resize)

#for videoCapture

capture = cv.VideoCapture('Videos/dog.mp4')
while True:
    isTrue,frame = capture.read()
        
    resize_frame = rescaleFrame(frame,0.2)
    cv.imshow('resize',resize_frame)
    
	if cv.waitKey(20) & 0xFF == ord('d'):
		break

capture.release()
capture.destroyAllWindows()



















