#!/usr/bin/python

import subprocess

from SimpleCV import Color, Image

import time

subprocess.call("raspistill -n -w %s -h %s -o Listing6_1.png"%(640,480),shell=True)

img=Image("Listing6_1.png")

img.show()
time.sleep(5)

circle=img.findCircle(canny=250,thresh=200,distance=11)
circle.draw(color=Color.BLACK, width=4)
circle.show()
time.sleep(5)

circle=circle.sortArea()
circle[0].draw(Color.RED,width=4)

img_with_circles=img.applyLayers()
img_with_cirlces.save("Listing6_2.png")

img_with_cirlces.show()
time.sleep(15)
