import cv2
import mediapipe as mp
import time

url = 'https://25.73.37.247:8080/video'
cap = cv2.VideoCapture(url)





mpHands = mp.solutions.hands
hands = mpHands.Hands()


mpDraw = mp.solutions.drawing_utils
pTime = 0
cTime = 0
 
while True:
	success,img = cap.read()

	#img = cv2.resize(img,(800,600),interpolation=cv2.INTER_AREA)

	imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
	results = hands.process(imgRGB)	

	#print(results.multi_hand_landmarks)


	if results.multi_hand_landmarks:
		for handLns in results.multi_hand_landmarks:
			for id,lm in enumerate(handLns.landmark):
				# print(ln)
				h,w,c = img.shape
				cx,cv = int(lm.x*w),int(lm.y*h)

				if id==0:
					cv2.circle(img,(cx,cv),24,(255,0,255),cv2.FILLED)



			mpDraw.draw_landmarks(img,handLns,mpHands.HAND_CONNECTIONS)



	cTime = time.time()
	fps = 1/(cTime-pTime)
	pTime = cTime

	cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,255),3)

	cv2.imshow('image',img)
	cv2.waitKey(1)


