import cv2

image = cv2.imread("../resource/pic.jpg")
cv2.imshow("Original", image)

enlarge  = cv2.resize(image, None, fx=1.2, fy=1.4, interpolation=cv2.INTER_LINEAR)
enlarge1 = cv2.resize(image, None, fx=1.2, fy=1.4, interpolation=cv2.INTER_CUBIC)

shrink = cv2.resize(image, None, fx=0.8, fy=0.6, interpolation=cv2.INTER_AREA)

cv2.imshow("Linear Enlarge", enlarge)
cv2.imshow("Cubic Enlarge", enlarge1)
cv2.imshow("Area Shrink", shrink)

cv2.waitKey(0)