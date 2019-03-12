import numpy as np
import cv2
import time
cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    #print(ret)
    #print(frame)
    # Our operations on the frame come here
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',frame)
    key=cv2.waitKey(1)
    #time.sleep(0.1)
    if key==27:
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()