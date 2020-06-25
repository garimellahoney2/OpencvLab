import numpy as np
import cv2

cap = cv2.VideoCapture(0)
count = 1
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    

    # Display the resulting frame
    cv2.imshow('frame',frame)
    cv2.imwrite('frame{:d}.jpg'.format(count), frame)
    frame1 = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame1',frame1)
    cv2.imwrite('frame1{:d}.jpg'.format(count), frame1)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    if(count==5):
        break
    count += 1

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
