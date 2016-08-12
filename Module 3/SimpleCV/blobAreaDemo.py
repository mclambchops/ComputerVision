#!/usr/bin/python

import subprocess
from SimpleCV import Image
import time

subprocess.call("raspistill -n -w %s -h %s -o Listing3_1.png"%(640,480),shell=True)

img=Image("Listing3_1.png")
img.show()

time.sleep(5)

img=img.binarize()
img.show()

time.sleep(5)

spots=img.findBlobs()
img.show()

time.sleep(5)

print "Areas: ", spots.area()
print "Angles: ", spots.angle()
print "Centers: ", spots.coordinates()


