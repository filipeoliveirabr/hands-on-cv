import cv2

image = cv2.imread("../resource/noisy.png")

blur_image = cv2.medianBlur(image, 7)
cv2.imshow("Original", image)
cv2.imshow("Corrected", blur_image)

cv2.waitKey(0)