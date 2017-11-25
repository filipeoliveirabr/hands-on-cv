import cv2
image = cv2.imread("coffee.jpg")

cv2.line(image, (20,21), (100,100), (255,0,0), 5 )
cv2.circle(image, (50,50), 50, (0,0,255), 2)
cv2.circle(image, (200,50), 50, (0,0,255), -1)
cv2.rectangle(image, (25,21),(200,200),(0,255,0),2)

cv2.imshow("Geometry Image", image)
cv2.waitKey(0)