#!/usr/bin/python

import time
from SimpleCV import Image, Color

img = Image("password.jpg")
keys = img.findKeypoints()
keys.draw(color=Color.BLUE)
img.show()
img.save('pic.jpg')
time.sleep(10)