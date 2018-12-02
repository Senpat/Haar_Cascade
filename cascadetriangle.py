#uses the cascade
#cascadetriangle.py video

import sys
import cv2

videopath = "C:\\Users\\zz198\\OneDrive\\Desktop\\RC\\testvideos\\redtriangle_Trim.mp4"
cap = cv2.VideoCapture(0)

triangle_cascade = cv2.CascadeClassifier("data/cascade.xml")

while cap.isOpened():
	ret,frame = cap.read()
	if(not ret):
		continue
	gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

	triangles = triangle_cascade.detectMultiScale(gray,50,50)

	for(x,y,w,h) in triangles:
		cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,0),2)

	cv2.imshow("frame",frame)

cap.release()
cv2.destroyAllWindows()
