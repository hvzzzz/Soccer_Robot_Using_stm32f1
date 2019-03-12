import numpy as np
import cv2
cap=cv2.VideoCapture(0)
while True:
    ret,frame=cap.read()
    hvs_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    cv2.imshow("frame",frame)
    key=cv2.waitKey(1)
    if key==27:
        break

