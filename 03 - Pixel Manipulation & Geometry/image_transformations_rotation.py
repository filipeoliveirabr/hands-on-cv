import cv2
import random
import numpy as np

image = cv2.imread("../resource/coffee.jpg")
(rows, cols, planes) = np.shape( image )
center = (cols // 2, rows // 2)

matrix   = cv2.getRotationMatrix2D(center, 45, 1)
rotation = cv2.warpAffine(image, matrix, (cols, rows))

cv2.imshow( "Original", image )
cv2.imshow( "Rotation", rotation )

cv2.waitKey(0)