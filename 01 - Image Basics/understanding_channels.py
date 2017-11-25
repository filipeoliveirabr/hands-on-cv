import cv2

pic = cv2.imread("../resource/messi2.png")
print("Original shape")
print(pic.shape)
print("\n")

(b, g, r) = cv2.split(pic)

#cv2.imshow("Blue", b)
#cv2.waitKey(0)


merged_image = cv2.merge((b,g,r))

print("Merged shape")
print(merged_image.shape)
print("\n")

#cv2.imshow("Merged",  merged_image)
#cv2.waitKey(0)

gray_image = cv2.cvtColor( merged_image, cv2.COLOR_BGR2GRAY)

print("Gray image")
print(gray_image.shape)

#cv2.imshow("Gray Image",  gray_image)
#cv2.waitKey(0)

