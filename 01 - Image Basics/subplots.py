#matplot->RGB  OPEN_CV->BGR

import cv2

from matplotlib import pyplot as plt

pic  = cv2.imread("../resource/messi2.png")
gray = cv2.cvtColor(pic, cv2.COLOR_BGR2GRAY)

tweaked_image = cv2.cvtColor(pic, cv2.COLOR_BGR2RGB)
figure = plt.figure()

plt.subplot(1,2,1), plt.title("Original Image"), plt.imshow(tweaked_image)
plt.subplot(1,2,2), plt.title("Grayscale Image"), plt.imshow(gray, cmap="gray")


plt.show()

