#!/usr/bin/python2.7

import picamera
import cv2
from SimpleCV import Image, Color


import time

with picamera.PiCamera() as camera:
	camera.resolution = (640,480)
	camera.start_preview()
	time.sleep(10)
	camera.capture('photo.jpg')
	photo=Image("photo.jpg")

	print(photo.listHaarFeatures())
	found = photo.findHaarFeatures('face.xml')
	if found:
		for find in found:
			print "Found all face coordinates :" + str(find.coordinates())
			find.draw()	
	else:		
		print "Not found"

	found2 = photo.findHaarFeatures('upper_body.xml')
	if found:
		for find in found2:
			print "Found all upper body coordinates :" + str(find.coordinates())
			find.draw(color=Color.BLUE)	
	else:		
		print "Not found"
	camera.stop_preview()
	photo.save('photo1.jpg')
	time.sleep(10)
