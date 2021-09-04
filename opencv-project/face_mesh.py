import cv2
import mediapipe as mp
import time





capture = cv2.VideoCapture('https://26.151.102.175:8080/video')
pTime = 0


mpDraw = mp.solutions.drawing_utils
mpFaceMesh = mp.solutions.face_mesh
faceMesh = mpFaceMesh.FaceMesh(max_num_faces=2)
drawSpec = mpDraw.DrawingSpec(thickness=1,circle_radius=2)


while True:
	success,img = capture.read()
	imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

	results = faceMesh.process(imgRGB)

	if results.multi_face_landmarks:
		for faceLns in results.multi_face_landmarks:

			for id,lm in enumerate(faceLns.landmark):
				

				ih,iw,ic = img.shape
				x,y = int(iw*lm.x),int(lm.y*ih)
				#print(id,x,y)


			mpDraw.draw_landmarks(img,faceLns,mpFaceMesh.FACE_CONNECTIONS,drawSpec,drawSpec)


	cTime = time.time()		
	fps = 1/(cTime-pTime)
	pTime = cTime


	cv2.putText(img,f"{int(fps)}",(20,70),cv2.FONT_HERSHEY_PLAIN,3,(0,255,0),3)


	cv2.imshow('image',img)		

	cv2.waitKey(1)

