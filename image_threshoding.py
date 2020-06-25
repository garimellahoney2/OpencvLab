# we don't use .pack we use .grid its like excel sheet
from tkinter import *
from cv2 import *
import numpy as np  
def binary():
    image1 = imread(r"C:\Users\Personal\Documents\3rdyear\lab_manuals\images.jpg")  

    img = cvtColor(image1, cv2.COLOR_BGR2GRAY) 

    ret, thresh1 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)#threshold value maximum value
    imshow('binary',thresh1)
    waitKey(0)
    destroyAllWindows()
root = Tk()
B = Button(text ="binary", command = binary)
B.grid(column=1)
root.mainloop()
