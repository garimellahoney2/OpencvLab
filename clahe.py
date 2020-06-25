import numpy as np
import cv2
clahe = cv2.createCLAHE(tileGridSize=(8,8))
img = cv2.imread(r"C:\Users\Personal\Documents\3rdyear\lab_manuals\images.jpg",0)
cl1 = clahe.apply(img)
cv2.imshow('helo',cl1)
cv2.waitKey(0)#wait after time
cv2.destroyAllWindows()
