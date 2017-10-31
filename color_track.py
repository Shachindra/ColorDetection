# Steps to get HSV Boundary Values
# color = np.uint8([[[0, 128, 0]]])
# hsv_green = cv2.cvtColor(green, cv2.COLOR_BGR2HSV)
# print (hsv_color)

import cv2
import numpy as np
print("OpenCV Version: "+cv2.__version__)
camera_port = 0
cap = cv2.VideoCapture(camera_port)

while(True):

	# Take each frame
	ret, frame = cap.read()
	
	# Convert BGR to HSV
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	# Defined range of colors in HSV
	lower_red = np.array([-10, 50, 50])
	upper_red = np.array([20, 255, 255])
	lower_blue = np.array([110, 50, 50])
	upper_blue = np.array([130, 255, 255])
	lower_yellow = np.array([20, 50, 50])
	upper_yellow = np.array([40, 255, 255])
	lower_green = np.array([50, 50, 50])
	upper_green = np.array([70, 255, 128])

	# Threshold the HSV image to get only the specified colors - Blue in this case
	mask = cv2.inRange(hsv, lower_blue, upper_blue)
	
	# Bitwise-AND mask and original image
	res = cv2.bitwise_and(frame, frame, mask = mask)
	
	cv2.imshow('frame', frame)
	cv2.imshow('mask', mask)
	cv2.imshow('res', res)
	
	# Press Esc to exit
	k = cv2.waitKey(5) & 0xFF
	if k == 27:
		break

cv2.destroyAllWindows()
