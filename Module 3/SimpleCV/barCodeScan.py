#!/usr/bin/python

import subprocess

from SimpleCV import Image, Barcode

import time

#subprocess.call("raspistill -n -w %s -h %s -o Listing7_1.png"%(640,480),shell=True)

img=Image("barcode.png")
img.show()
time.sleep(5)

barcode = img.findBarcode()

print barcode[0].data