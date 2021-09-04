import cv2
import mediapipe as mp
import time
 
cap = cv2.VideoCapture('https://25.245.102.127:8080/video')

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0



while True:
	success,img = cap.read()
	imgRGB = cv2.cvtColor(img,cv.COLOR_BGR2RGB)
	