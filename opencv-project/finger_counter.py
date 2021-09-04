import cv2
import mediapipe as mp
import hand_tracking_module as htm
import time
import os


URL = 'https://26.151.102.175:8080/video'

cap = cv2.VideoCapture(URL)
pTime = 0


folderPath = "FingerImages"
myList = os.listdir(folderPath)

overlayList = []

for imPath in myList:
	image = cv2.imread(f"{folderPath}/{imPath}")
	#image = cv2.resize(image,(200,200),interpolation=cv2.INTER_AREA)
	overlayList.append(image)


detector = htm.handDetector(detectionCon=0.75)

tipIds = [4,8,12,16,20]


while True:
	success,img = cap.read()
	img = cv2.resize(img,(800,600),interpolation=cv2.INTER_AREA)
	img = detector.findHands(img) 
	lmList = detector.findPosition(img,draw=False)

	if len(lmList) !=0:
		fingers = []

		# thumb
		if lmList[tipIds[0]][1] > lmList[tipIds[0]-1][1]:
				
			fingers.append(1)

		else:
			fingers.append(0)
			


		for id in range(1,5):
			if lmList[tipIds[id]][2] < lmList[tipIds[id]-2][2]:
				#print("Index finder open")
				fingers.append(1)

			else:
				fingers.append(0)
			
		print(fingers)		


		total_fingers = fingers.count(1)


		h,w,c = overlayList[total_fingers-1].shape
		img[0:h,0:w] = overlayList[total_fingers-1]





	# cTime = time.time()	
	# print(f"{cTime} {pTime}")	
	# fps = 1/(cTime-pTime)
	# pTime = cTime


	# cv2.putText(img,f"{int(fps)}",(20,70),cv2.FONT_HERSHEY_PLAIN,3,(0,255,0),3)



	cv2.imshow('img',img)
	cv2.waitKey(1)
