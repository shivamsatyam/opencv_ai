import cv2
import mediapipe as mp
import math


class poseDetector:

	def __init__(self,mode=False,upBody=False,smooth=True,detectionCon=0.5,trackCon=0.5):

		self.mode = mode
		self.upBody = upBody
		self.smooth = smooth
		self.detectionCon = detectionCon
		self.trackCon = trackCon


		self.mpPose = mp.solutions.pose
		self.pose = self.mpPose.Pose(self.mode,self.upBody,self.smooth,self.detectionCon,self.trackCon)

		self.mpDraw = mp.solutions.drawing_utils




	def findPose(self,img,draw=True):
		imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
		self.results = self.pose.process(imgRGB)


	

		if self.results.pose_landmarks:
			if draw:
				self.mpDraw.draw_landmarks(img,self.results.pose_landmarks,self.mpPose.POSE_CONNECTIONS)
		
		return img		


	def findPosition(self,img,draw=True):
			
		self.lmList = []
			
		if self.results.pose_landmarks:

			for id,lm in enumerate(self.results.pose_landmarks.landmark):
				h,w,c = img.shape
				cx,cv = int(lm.x*w),int(lm.y*h)
				self.lmList.append([id,cx,cv])
				if draw:
					cv2.circle(img,(cx,cv),14,(255,0,255),cv2.FILLED)

		return self.lmList			



	def findAngle(self,img,p1,p2,p3,draw=True):	
		x1,y1 = self.lmList[p1][1:]
		x2,y2 = self.lmList[p2][1:]
		x3,y3 = self.lmList[p3][1:]


		# calculate the angle

		# angle = (math.atan2((y3-y2,x3-x2)-math.atan2(y1-y2,x1-x2)))

		angle = math.degrees(math.atan2(y3-y2,x3-x2)-math.atan2(y1-y2,x1-x2))

		if angle<0:
			angle +=360


		# print(int(angle))
		if draw:
			
			cv2.line(img,(x1,y2),(x2,y2),(255,255,255),3)
			cv2.line(img,(x3,y3),(x2,y2),(255,255,255),3)

			cv2.circle(img,(x1,y1),8,(255,0,5),cv2.FILLED)
			cv2.circle(img,(x1,y1),15,(255,0,5),2)
			cv2.circle(img,(x2,y2),8,(255,0,5),cv2.FILLED)
			cv2.circle(img,(x2,y2),15,(255,0,5),2)
			cv2.circle(img,(x3,y3),8,(255,0,5),cv2.FILLED)
			cv2.circle(img,(x3,y3),15,(255,0,5),2)

			cv2.putText(img,str(int(angle)),(x2-50,y2+50),cv2.FONT_HERSHEY_PLAIN,2,(255,0,255),2)

		return angle	


def main():
	cap = cv2.VideoCapture('Pexels Videos 2785536_480x854.mp4')

	detector = poseDetector()

	while True:
		success,img = cap.read()
		img = detector.findPose(img)
		lmList = detector.findPosition(img,draw=False)


		cv2.imshow('Image',img)

		cv2.waitKey(1)




if __name__ == '__main__':
	main()
