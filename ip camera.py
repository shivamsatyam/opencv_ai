
import cv2
import numpy as np

url = 'https://10.136.111.42:8080/video'
cp = cv2.VideoCapture(url)


while True:
	camera,frame = cp.read()
	if frame is not None:
		cv2.imshow("Frame",frame)

	q = cv2.waitKey(1)

	if q==ord('q'):
		break	
 

cp.release()
cv2.destroyAllWindows()






