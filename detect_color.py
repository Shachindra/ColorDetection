import cv2
import numpy as np
import imutils

# Load an Image and Convert it to HSV
frame = cv2.imread("./images/not_charging.jpg", 1)
image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

circularKernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
(row, height, column, width) = cv2.selectROI("ROI Selector", image, fromCenter = False, showCrosshair = False)

# Create Mask
image_crop = image[height:height + width, row:row + column]

# Create the color mappings for upper and lower boundary values for HSV or LaB depending on accuracy required

# Now After the ROI is found get the color value obtained from the values in the shape

# Display cropped image
cv2.imshow("Image", image_crop)
cv2.waitKey(0)