#uses the cascade
#cascadetriangle.py video

import sys
import cv2
import numpy as np
import imutils

videopath = "whitetriangle.mp4"
cap = cv2.VideoCapture(videopath)

triangle_cascade = cv2.CascadeClassifier("data/cascade.xml")

while True:
	ret,frame = cap.read()
	frame = imutils.resize(frame,width = 146,height = 86)						#raw is 364,216
	#frame = imutils.resize(frame,width = 80,height = 50)						#for pentagon
	#frame = imutils.resize(frame,width = 364,height=85)
	gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

	triangles = triangle_cascade.detectMultiScale(gray,50)

	for(x,y,w,h) in triangles:
		print((x,y,w,h))
		cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,0),2)

	cv2.imshow("frame",frame)

	k = cv2.waitKey(30) & 0xff
	if(k==27):
		break

cap.release()
cv2.destroyAllWindows()
