import cv2
import random
import numpy as np
import random
image = cv2.imread('../resource/janice.png')
gray  = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY) 
blurred = cv2.GaussianBlur(gray,(9,9),0)
th1= cv2.adaptiveThreshold(blurred,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,1)
(rows,cols) = np.shape(th1)
canvas = np.zeros((rows,cols,3), dtype= "uint8")
for i in range(0,rows):
	for j in range(0,cols):
		for k in range(0,3): # k is the iterator for number of planes
			if th1[i][j] != 0 :
				color = random.randrange(0,255,1)
				canvas[i][j][k]= color #(0,255,0)
			else:
				color = 0
				canvas[i][j][k] = color

cv2.imshow("Original",th1)
cv2.imshow("Canvas",canvas)
cv2.waitKey(0)