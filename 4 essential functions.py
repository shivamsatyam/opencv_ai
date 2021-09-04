import cv2 as cv

img = cv.imread('Photos/lady.jpg')

"""converting to grayscale"""

# gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY) # src,code,dst=None,dstCn=None
# cv.imshow('gray',gray)

# def videoToGrayScale():
#     capture = cv.VideoCapture("Videos/dog.mp4")
#     while True:
#         isTrue,frame = capture.read()
#         grayFrame = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
#         cv.imshow('image',grayFrame)
    
#         if cv.waitKey(20) & 0xFF==ord('d'):
#             break;
#     capture.release()
#     cv.destroyAllWindows()

# videoToGrayScale()



"""blur"""
# blur = cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT) # src,ksize,sigmaX,dst=None,sigmaY=None,borderType
# cv.imshow('image',blur)


"""edge cascade"""
# canny = cv.Canny(img,125,175) # image,threshold1,threshold2
# cv.imshow('image',canny)


"""dialated image"""
# dialated = cv.dilate(canny,(3,3),iterations=7)
# cv.imshow('dilated',dialated)


"""erode image"""
# erode = cv.erode(dialated,(3,3),iterations=3)
# cv.imshow('erode',erode)


"""resize"""

# resize1 = cv.resize(img,(200,200))
# resize2 = cv.resize(img,(200,200),interpolation=cv.INTER_AREA)
# resize3 = cv.resize(img,(1200,800),interpolation=cv.INTER_CUBIC)
# cv.imshow('resize1',resize1)
# cv.imshow('resize2',resize2)
# cv.imshow('resize3',resize3)


"""cropped"""

crop = img[50:100,150:300]
cv.imshow('crop',crop)

cv.waitKey(0)































