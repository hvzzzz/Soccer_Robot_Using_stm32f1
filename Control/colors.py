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
    low_red =np.array([0,110 ,156])
    high_red =np.array([14,231,255])
    #green ones
    #green_hvs=np.array([108,56,56])
    minHSV = np.array([73,49,70])
    maxHSV = np.array([90,171,202])
    maskr=cv2.inRange(hvs_frame,low_red,high_red)
    #red = cv2.bitwise_and(frame,frame,mask=maskr)
    maskgreen=cv2.inRange(hvs_frame,minHSV,maxHSV)
    mask=maskgreen|maskr
    red = cv2.bitwise_and(frame,frame,mask=mask)
    cv2.imshow("frame",frame)
    cv2.imshow("Detected",red)
    #print(maskr.shape)
    #print(frame.shape)
    key=cv2.waitKey(1)
    if key==27:
        break
cap.release()
cv2.destroyAllWindows()
