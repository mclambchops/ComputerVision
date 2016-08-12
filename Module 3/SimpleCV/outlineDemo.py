#!/usr/bin/python

import subprocess

from SimpleCV import Color, Image

import time

subprocess.call("raspistill -n -w %s -h %s -o Listing4_1.png"%(640,480),shell=True)

img=Image("Listing4_1.png")

img.show()
time.sleep(5)

color = (148.0, 128.0, 55.0)

yellow_distance=img.colorDistance(color).invert()

blobs = yellow_distance.findBlobs()

blobs.draw(color=Color.BLACK,width=4)

yellow_distance.save("Listing4_2.png")

yellow_distance.show()

time.sleep(5)

img.addDrawingLayer(yellow_distance.dl())

img.save("Listing4_3.png")

img.show()

time.sleep(5)
