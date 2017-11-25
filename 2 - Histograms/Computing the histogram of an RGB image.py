#references: 
# 1) https://en.wikipedia.org/wiki/Image_histogram
# 2) https://docs.opencv.org/3.1.0/d1/db7/tutorial_py_histogram_begins.html#gsc.tab=0
# 3) http://www.cambridgeincolour.com/tutorials/histograms1.htm
# 4 http://www.cambridgeincolour.com/tutorials/histograms2.htm

import cv2
from matplotlib import pyplot as plt

messi = cv2.imread("messi2.png")

b_hist = cv2.calcHist([messi], [0], None, [256], [0,256])
g_hist = cv2.calcHist([messi], [1], None, [256], [0,256])
r_hist = cv2.calcHist([messi], [2], None, [256], [0,256])

plt.figure()
plt.xlabel("Intensity Levels")
plt.ylabel("Number of Pixels")

plt.plot(b_hist, color="b"), plt.xlim([-20,300])
plt.plot(g_hist, color="g"), plt.xlim([-20,300])
plt.plot(r_hist, color="r"), plt.xlim([-20,300])

plt.show()