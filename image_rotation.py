#https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_geometric_transformations/py_geometric_transformations.html#transformations
import cv2
img = cv2.imread(r"C:\Users\Personal\Documents\3rdyear\lab_manuals\noised_image.jpg",0)
rows,cols = img.shape#it only works for black and white because for colour we have 3 matrices
while(1):
    flag = 0
    for i in range(1,361):
        M = cv2.getRotationMatrix2D((cols/2,rows/2),i,1)#this is transformation matrix first parametre is to define centre,angle for rotation,scale
        dst = cv2.warpAffine(img,M,(cols,rows))
        cv2.imshow('hello',dst)#it overwrites
        
        if(cv2.waitKey(1)&0xFF==ord('q')):#waitkey returns 32bits but we want 8bit so we use bitwise operator to get last 8bits here 0xFF is 8 ones
            flag = 1
            break
    if(flag):
        break
    
cv2.destroyAllWindows()
