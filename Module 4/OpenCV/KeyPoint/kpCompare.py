import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('password.jpg',0)
img2 = cv2.imread('passwordmatch.jpg',0)

sift = cv2.xfeatures2d.SIFT_create()

kp1, des1 = sift.detectAndCompute(img,None)
kp2, des2 = sift.detectAndCompute(img2,None)

bf = cv2.BFMatcher()

matches = bf.knnMatch(des1,des2,k=2)

good=[]
for m,n in matches:
    if m.distance<0.75*n.distance:
        good.append([m])


img3 = cv2.drawMatchesKnn(img,kp1,img2,kp2,matches,None,flags=2)

plt.imshow(img3,),plt.show()
