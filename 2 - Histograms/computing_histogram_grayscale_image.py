import cv2
from matplotlib import pyplot as plt 


image = cv2.imread('../resource/messi2.png')
grayscale = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow("gray image",grayscale)
cv2.waitKey(0)

#calculate the histogram now 
histogram = cv2.calcHist([grayscale],[0],None,[256],[0,255])
plt.figure()
plt.xlim([0,255])
plt.xlabel(" pixel intensities")
plt.ylabel(" number of pixels ")
plt.plot(histogram,color="r")
plt.show()