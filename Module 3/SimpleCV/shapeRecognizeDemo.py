#!/usr/bin/python

import subprocess

from SimpleCV import Color, Image

import time

subprocess.call("raspistill -n -w %s -h %s -o Listing5_1.png"%(640,480),shell=True)

img=Image("Listing5_1.png")

img.show()
time.sleep(5)

lines=img.findLines(threshold=30)
lines.draw(color=Color.BLACK, width=4)

img.save("Listing5_2.png")

img.show()

time.sleep(15)