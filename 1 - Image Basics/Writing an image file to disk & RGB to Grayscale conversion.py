import cv2

coffePic = cv2.imread("coffee.jpg")

gray_image = cv2.cvtColor(coffePic, cv2.COLOR_BGR2GRAY)

cv2.imshow("Grayed image", gray_image)

cv2.imwrite("gray_file.jpg", gray_image)
cv2.waitKey(0)