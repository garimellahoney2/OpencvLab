import cv2 as cv
import numpy as np

kernel = np.ones((5,5),np.uint8)
image = cv.imread(r"C:\Users\Personal\Pictures\galaxy.JPG",0)
tophat = cv.morphologyEx(image, cv.MORPH_TOPHAT, kernel)
cv.imshow("input",image)
cv.imshow("tophat",tophat)

cv.waitKey(0)
cv.destroyAllWindows()
