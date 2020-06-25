#https://www.learnopencv.com/how-to-select-a-bounding-box-roi-in-opencv-cpp-python/
import cv2
im = cv2.imread(r"C:\Users\Personal\Documents\3rdyear\lab_manuals\images.jpg")
r = cv2.selectROI(im)
imCrop = im[int(r[1]):int(r[1]+r[3]),int(r[0]):int(r[0]+r[2])]
cv2.imshow("image",imCrop)
cv2.waitKey(0)
cv2.destroyAllWindows()
