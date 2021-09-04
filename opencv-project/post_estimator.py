import cv2
import mediapipe as mp



mpPose = mp.solutions.pose
pose = mpPose.Pose()

mpDraw = mp.solutions.drawing_utils


cap = cv2.VideoCapture('pexels-rodnae-productions-7187116_480x854.mp4')


while True:
	success,img = cap.read()
	imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

	results = pose.process(imgRGB)
	#print(results.pose_landmarks)

	if results.pose_landmarks:
		for id,lm in enumerate(results.pose_landmarks.landmark):
			h,w,c = img.shape
			cx,cv = int(lm.x*w),int(lm.y*h)
			cv2.circle(img,(cx,cv),14,(255,0,255),cv2.FILLED)



		mpDraw.draw_landmarks(img,results.pose_landmarks,mpPose.POSE_CONNECTIONS)




	cv2.imshow('Image',img)

	cv2.waitKey(1)

