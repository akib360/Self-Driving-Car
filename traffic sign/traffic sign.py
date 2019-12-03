import cv2
import numpy as np
import os, sys, time
import serial


stop_sign = cv2.CascadeClassifier('C:/Users/akib/Desktop/autonomous car/traffic sign/cascade_xml/stop_sign.xml')
yield_sign = cv2.CascadeClassifier('C:/Users/akib/Desktop/autonomous car/traffic sign/cascade_xml/Speedlimit_24_15Stages.xml')
traffic_light = cv2.CascadeClassifier('C:/Users/akib/Desktop/autonomous car/traffic sign/cascade_xml/traffic_light.xml')

#ser1 = serial.Serial('COM9',9600)#change COM port number on which your arduino is connected
#arduino_data = 0
cap = cv2.VideoCapture(0)

time.sleep(0)


while True:
	(grabbed, img) = cap.read()
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	stop = stop_sign.detectMultiScale(gray, 1.5, 5)
	yield1 = yield_sign.detectMultiScale(gray, 1.5, 5)
	traffic = traffic_light.detectMultiScale(gray, 1.5, 5)

	for(x,y,w,h) in stop:
		cv2.rectangle(img, (x,y), ((x+w),(y+h)), (0, 128, 255), 2)
		#cv2.putText(image, 'OpenCV', org, font, fontScale, color, thickness, cv2.LINE_AA)

		cv2.putText(img, 'Stop', (x-w+190,y-5), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 128, 255), 4, cv2.LINE_AA)


	for(x,y,w,h) in yield1:
		cv2.rectangle(img, (x,y), ((x+w),(y+h)), (0, 128, 255), 2)
		#cv2.putText(image, 'OpenCV', org, font, fontScale, color, thickness, cv2.LINE_AA)
		cv2.putText(img, 'speed limit 24km/h', (x-w+190,y-5), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 128, 255), 4, cv2.LINE_AA)

	for(x,y,w,h) in traffic:
		cv2.rectangle(img, (x,y), ((x+w),(y+h)), (0, 128, 255), 2)
		#cv2.putText(image, 'OpenCV', org, font, fontScale, color, thickness, cv2.LINE_AA)
		cv2.putText(img, 'traffic-light', (x-w+190,y-5), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 128, 255), 4, cv2.LINE_AA)

	cv2.imshow('frame', img)






	if cv2.waitKey(1) == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()
