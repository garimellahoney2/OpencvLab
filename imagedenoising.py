import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread(r"C:\Users\Personal\Documents\3rdyear\p&cv\frame1.jpg")

dst = cv2.fastNlMeansDenoisingColored(img,None,10,10,7,21)

plt.subplot(121),plt.imshow(img)
plt.subplot(122),plt.imshow(dst)
plt.show()
