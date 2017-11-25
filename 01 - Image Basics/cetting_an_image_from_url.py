#REMEBER -> skimage read in RGB format
#OPENCV -> Used BGR convention

import cv2

from skimage import io
from matplotlib import pyplot as plt

joker = io.imread("https://s.aficionados.com.br/imagens/descubra-a-origem-misteriosa-do-coringa-o-rei-palhaco-do-crime_f.png")
cv2.imshow("Joker from URL", joker);

cv2.waitKey(0)

converted_image = cv2.cvtColor(joker, cv2.COLOR_BGR2RGB)
cv2.imshow("Joker right color", converted_image);
cv2.waitKey(0)

#plt.subplot(1,2,1), plt.title("Joker RGB normal"), plt.imshow(joker)
#plt.show()