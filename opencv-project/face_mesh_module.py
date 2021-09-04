import cv2
import mediapipe as mp
import time




class FaceMeshDetector():

	def __init__(self,staticMode=False,maxFaces=2,minDetectionCon=0.5,minTrackCon=0.5):

		self.staticMode = staticMode
		self.maxFaces =maxFaces 
		self.minDetectionCon = minDetectionCon
		self.minTrackCon = minTrackCon




		self.mpDraw = mp.solutions.drawing_utils
		self.mpFaceMesh = mp.solutions.face_mesh
		self.faceMesh = self.mpFaceMesh.FaceMesh(self.staticMode,self.maxFaces,self.minDetectionCon,self.minTrackCon)
		self.drawSpec = self.mpDraw.DrawingSpec(thickness=1,circle_radius=2)


	def findFaceMesh(self,img,draw=True):

		self.imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

		self.results = self.faceMesh.process(self.imgRGB)

		faces = []
		
		if self.results.multi_face_landmarks:

			

			for faceLns in self.results.multi_face_landmarks:
				
				if draw:
					self.mpDraw.draw_landmarks(img,faceLns,self.mpFaceMesh.FACE_CONNECTIONS,self.drawSpec,self.drawSpec)

				face = []	
					
				for id,lm in enumerate(faceLns.landmark):
					

					ih,iw,ic = img.shape
					x,y = int(iw*lm.x),int(lm.y*ih)
					#print(id,x,y)


					#cv2.putText(img,str(id),(x,y),cv2.FONT_HERSHEY_PLAIN,0.7,(,255,0),1)


					face.append([x,y])

				faces.append(face)		

		return img,faces		



def main():


	capture = cv2.VideoCapture('video (1)_640x360.mp4')
	pTime = 0

	detector = FaceMeshDetector()


	while True:	
		success,img = capture.read()
		img,faces = detector.findFaceMesh(img)
		cTime = time.time()		
		fps = 1/(cTime-pTime)
		pTime = cTime


		cv2.putText(img,f"{int(fps)}",(20,70),cv2.FONT_HERSHEY_PLAIN,3,(0,255,0),3)


		cv2.imshow('image',img)		

		cv2.waitKey(1)



if __name__ == '__main__':
	main()