import cv2

image = cv2.imread("../resource/hello.png")
cv2.imshow("Original",image)
cv2.waitKey(0)