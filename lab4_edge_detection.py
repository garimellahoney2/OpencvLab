import cv2
image = cv2.imread(r"C:\Users\Personal\Documents\3rdyear\lab_manuals\images.jpg")
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow('gray',gray)
ds = cv2.GaussianBlur(gray,(3,3),cv2.BORDER_WRAP)#Specifies image boundaries
cv2.imshow('gray1',ds)
des = cv2.Sobel(gray,-1,1,1)
cv2.imshow('gray3',des)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
Sobel(src, dst, ddepth, dx, dy) for c++
This method accepts the following parameters −

src − An object of the class Mat representing the source (input) image.

dst − An object of the class Mat representing the destination (output) image.

ddepth − An integer variable representing the depth of the image (-1)

dx − An integer variable representing the x-derivative. (0 or 1)

dy − An integer variable representing the y-derivative. (0 or 1)
'''

