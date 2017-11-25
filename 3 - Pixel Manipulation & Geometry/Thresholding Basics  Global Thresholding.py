import cv2

image = cv2.imread("pic.jpg")
gray  = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY)

cv2.imshow("Orignal", image)
cv2.imshow("Gray", gray)
cv2.imshow("Thresholded image", thresh)

cv2.waitKey(0)