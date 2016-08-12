import sys
import time
from picamera.array import PiRGBArray
from picamera import PiCamera
import cv2

mainLoop=True
cascPath = "/home/pi/Desktop/ComputerVision/Module 4/FaceDetect/haarcascade_frontalface_default.xml"

camera = PiCamera()
rawCap = PiRGBArray(camera)
time.sleep(5)
camera.capture(rawCap, format="bgr")
image = rawCap.array

try:
    password=cv2.imread("photo.jpg",0) #passing 0 autoconverts image to grayscale
    print 'password read'
except:
    password=None

#while mainLoop:
    #image = cv2.imread(image,0)
    #gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

print 'loop start'
faceCascade = cv2.CascadeClassifier(cascPath)
faces = faceCascade.detectMultiScale(
    image,#gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize =(30,30),
    flags = cv2.CASCADE_SCALE_IMAGE
    )
minMatch = 20 #minimum number of keypoint matches to pass facial recognition test

if faces.size > 0:
   if password.size < 1:
        password = cv2.imgwrite("photo.jpg", image, IMWRITE_JPEG_OPTIMIZE)
        mainLoop=False

   else:
        sift=cv2.xfeatures2d.SIFT_create()
        kp1, des1=sift.detectAndCompute(password,None)
        kp2, des2=sift.detectAndCompute(image,None)
        bf = cv2.BFMatcher()
        matches = bf.knnMatch(des1,des2,k=2)
        good=[]
        for m,n in matches:
            if m.distance<0.75*n.distance:
                good.append([m])

        if len(good)>= minMatch:
            print("Welcome back!")
            mainLoop=False

        else:
            print("INTRUDER!!!")
            mainLoop=False
else:
    print 'No face detected'
