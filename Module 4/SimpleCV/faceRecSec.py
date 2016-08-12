import picamera
from SimpleCV import Image, Color
import time

quality = 400
minMatch=0.3

try:
	password = Image("password.jpg")
except:
	password = None

mode="unsaved"
saved=False
minDist=0.25

with picamera.PiCamera() as camera:
	while True:
		camera.start_preview()
		time.sleep(10)
		camera.capture('pifacepw.jpg')
		img=Image("pifacepw.jpg")
		camera.stop_preview()
		
		faces = img.findHaarFeatures("face.xml")
		if faces:
			if not password:
				faces.draw()
				face=faces[-1]
				password = face.crop().save("password.jpg")
				print "Saving photo for security reference"
				print "Terminating program"
				break
			else:
				faces.draw()
				face=faces[-1]
				template = face.crop()
				template.save("passwordmatch.jpg")
				keypoints = password.findKeypointMatch(template, quality,minDist, minMatch)
				print 'ok'
				if keypoints:
					print "Welcome back"
					demand = raw_input("Do you want to use last photo for password? y/n").strip()
					if demand == "y":
						image=cam.getImage().scale(320,240)
						faces = image.findHaarFeatures("face.xml")
						tryit += 1
						while not tryit == 10 or not faces:
							image = cam.getImage().scale(320, 240)
							faces = image.findHaarFeatures("face.xml")
							tryit += 1
						if not faces:
							"No face found"
							break
						else:
							faces.draw()
							face = faces[-1]
							password = face.crop().save("password.jpg")
							face.crop().show()
							print "Saved!"
							print "Stop program."
							time.sleep(1)
							break
					else:
						print "OK..."
						break
				else:
					print "Not recognized"
					print "Activate alarm!"
					break
		else:
			break