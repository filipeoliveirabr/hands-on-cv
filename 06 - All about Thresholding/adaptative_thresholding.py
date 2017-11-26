import cv2

image = cv2.imread('../resource/pic.jpg')
gray  = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow("Gray", gray)

gray = cv2.GaussianBlur(gray, (9,9),0)
cv2.imshow("Gray Blur", gray)

ret, th = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY )

#th1 = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 1)

th1 = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 1)

cv2.imshow("Orignal image", image)
cv2.imshow("Threasholded Global", th)
cv2.imshow("Threashholded Adaptive", th1)

cv2.waitKey(0)