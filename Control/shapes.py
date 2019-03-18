import numpy as np
import cv2
import time
cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lower_red=np.array([0,0,0])
    upper_red=np.array([180,255,255])
    mask=cv2.inRange(hsv,lower_red,upper_red)
    #print(ret)
    #print(frame)
    # Our operations on the frame come here
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',frame)
    cv2.imshow('red',mask)
    key=cv2.waitKey(1)
    if key==27:
        break
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()