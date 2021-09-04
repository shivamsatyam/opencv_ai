import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('Photos/cats.jpg')
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

blank  = np.zeros(img.shape[:2],dtype="uint8")

circle = cv.circle(blank,(img.shape[1]//2,img.shape[0]//2),100,255,-1)

mask = cv.bitwise_and(gray,gray,mask=circle)

# gray_hist = cv.calcHist([gray],[0],None,[256],[0,256]) # images,channels,mask,histSize,ranges,hist=None,accumulate=None
# gray_hist = cv.calcHist([gray],[0],mask,[256],[0,256]) # images,channels,mask,histSize,ranges,hist=None,accumulate=None


# plt.figure()
# plt.title("histogram")
# plt.xlabel("bins")
# plt.ylabel("no of pixel")
# plt.plot(gray_hist)
# plt.xlim([0,256])
# plt.show()



"""color images"""

newmask = cv.bitwise_and(img,img,mask=circle)
colors = ('b','g','r')

plt.figure()
plt.title("histogram")
plt.xlabel("bins")
plt.ylabel("no of pixel")
for i,col in enumerate(colors):
    hist = cv.calcHist([img],[i],None,[256],[0,256])
    plt.plot(hist,color=col)
    
plt.show()

cv.waitKey(0)










































