import numpy as np
import cv2
cap=cv2.VideoCapture(0)
thresh=40
while True:
    ret,frame=cap.read()
    #brightHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #bgr = [40, 158, 16]
    #green_hvs = cv2.cvtColor( np.uint8([[bgr]] ), cv2.COLOR_BGR2HSV)[0][0]
    hvs_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    #red ones
    low_red =np.array([0,19 ,0])
    high_red =np.array([113,221,156])
    #green ones
    #green_hvs=np.array([108,56,56])
    #minHSV = np.array([green_hvs[0] - thresh, green_hvs[1] - thresh, green_hvs[2] - thresh])
    #maxHSV = np.array([green_hvs[0] + thresh, green_hvs[1] + thresh, green_hvs[2] + thresh])
    mask=cv2.inRange(hvs_frame,low_red,high_red)
    red = cv2.bitwise_and(frame,frame,mask=mask)
    #maskgreen=cv2.inRange(brightHSV,minHSV,maxHSV)
    cv2.imshow("frame",frame)
    cv2.imshow("Detected",red)
    key=cv2.waitKey(1)
    if key==27:
        break
cap.release()
cv2.destroyAllWindows()
