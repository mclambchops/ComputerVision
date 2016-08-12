#!/usr/bin/python

import subprocess
from SimpleCV import Image
import time

subprocess.call("raspistill -n -w %s -h %s -o Listing2_1.png"%(640,480),shell=True)

img=Image("Listing2_1.png")
img.show()

time.sleep(5)
img=img.binarize()
img.show()

time.sleep(5)
spots=img.findBlobs()
img.save("Listing2_2.png")
img.show()
time.sleep(20)

#print(spots)