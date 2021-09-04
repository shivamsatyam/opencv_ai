import cv2 as cv

"""
#reading images

img = cv.imread('Photos/cat.jpg')
cv.imshow('cat',img)
cv.waitKey(0)

"""


#reading videos

capture = cv.VideoCapture('Videos/dog.mp4')
while True:
	isTrue,frame = capture.read() # read the video frame by frame and return a boolean for succesfylly captured
	cv.imshow('Video',frame)
	# print(f"waitkey {cv.wail}")
	if cv.waitKey(20) & 0xFF == ord('d'):
		break

capture.release()
cv.destroyAllWindows()



