import cv2
import mediapipe as mp
import time


class handDetector():
	def __init__(self,mode=False,maxHands=2,detectionCon=0.5,trackCon=0.5):
		
		self.mode = mode
		self.maxHands = maxHands
		self.detectionCon = detectionCon
		self.trackCon = trackCon


		self.mpHands = mp.solutions.hands
		self.hands = self.mpHands.Hands(self.mode,self.maxHands,self.detectionCon,self.trackCon)
		self.mpDraw = mp.solutions.drawing_utils
		self.tipIds = [4,8,12,16,20]


	def findHands(self,img,draw=True):	
		imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
		self.results = self.hands.process(imgRGB)	

		if self.results.multi_hand_landmarks:
			for handLns in self.results.multi_hand_landmarks:
				
				if draw:	
					self.mpDraw.draw_landmarks(img,handLns,self.mpHands.HAND_CONNECTIONS)


		return img			



	def findPosition(self,img,handNo=0,draw=True):		

		self.lmList = []

		if self.results.multi_hand_landmarks:
			
			myHand = self.results.multi_hand_landmarks[handNo]

			for id,lm in enumerate(myHand.landmark):
			
				# print(ln)
				h,w,c = img.shape
				cx,cv = int(lm.x*w),int(lm.y*h)

				self.lmList.append([id,cx,cv])
				
				if draw:
					cv2.circle(img,(cx,cv),7,(255,0,255),cv2.FILLED)


		return self.lmList	



	def fingersUp(self):
		fingers = []

		# thumb
		if self.lmList[self.tipIds[0]][1] < self.lmList[self.tipIds[0]-1][1]:
				
			fingers.append(1)

		else:
			fingers.append(0)
			


		for id in range(1,5):
			if self.lmList[self.tipIds[id]][2] < self.lmList[self.tipIds[id]-2][2]:
				#print("Index finder open")
				fingers.append(1)

			else:
				fingers.append(0)
	
		return fingers	

def main():
	pTime = 0
	cTime = 0
	
	url = 'https://10.173.90.239:8080/video'
	cap = cv2.VideoCapture(url)

	detector = handDetector()

	while True:
		success,img = cap.read()
		img = detector.findHands()
		lmList = detector.findPosition()

		if len(lmList) !=0:
			print(lmList[4])

		cTime = time.time()
		fps = 1/(cTime-pTime)
		pTime = cTime

		cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,255),3)

		cv2.imshow('image',img)
		cv2.waitKey(1)





if __name__ == '__name__':
	main()