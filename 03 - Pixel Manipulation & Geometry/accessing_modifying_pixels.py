import cv2
image = cv2.imread("../resource/coffee.jpg")

pixel = image[300, 320]
print(pixel)

image[300:320, 300:320] = (255,0,0)
cv2.imshow("Modifed image", image)
cv2.waitKey(0)