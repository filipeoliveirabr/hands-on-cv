import cv2

image = cv2.imread("pic.jpg")

hor  = cv2.flip(image, 1)
vert = cv2.flip(image, 0)

both = cv2.flip(image, -1)

cv2.imshow("Original", image)
cv2.imshow("Both flip", both)

cv2.waitKey(0) 