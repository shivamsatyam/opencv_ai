import cv2
import mediapipe as mp
import time
import pose_estimater_module as pm
from numpy import interp


cap = cv2.VideoCapture('videos/production ID_4259068_854x480.mp4')
pTime = 0
detector  = pm.poseDetector()
count = 0
dir = 0

while True:
	success,img = cap.read()
	img = cv2.resize(img,(800,600),interpolation=cv2.INTER_AREA)

	img = detector.findPose(img)
	lmList  = detector.findPosition(img,False)


	if len(lmList) !=0:
		angle = detector.findAngle(img,11,13,15)
		# detector.findAngle(img,12,14,16)

		per = interp(angle,(186,334),(0,100))
		print(per)

		# check for the dumbell curls

		if per==100:
			if dir== 0:
				count+=0.5

		if per==0:
			if dir == 1:
				count+=0.5		
				dir = 0

		print(count)		

		cv2.rectangle(img,(0,450),(250,720),(0,255,0),cv2.FILLED)
		cv2.putText(img,f"{int(count)}",(65,560),cv2.FONT_HERSHEY_PLAIN,5,(255,0,255),5)


		cv2.putText(img,f"{int(count)}",(50,100),cv2.FONT_HERSHEY_PLAIN,5,(255,0,0),5)

	cv2.imshow('image',img)

	cv2.waitKey(1)
