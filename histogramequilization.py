import cv2
img = cv2.imread(r"C:\Users\Personal\Documents\3rdyear\lab_manuals\images.jpg",0)
img1 = cv2.equalizeHist(img)
cv2.imshow("hello",img1)
cv2.waitKey(0)
cv2.destroyAllWindows()

