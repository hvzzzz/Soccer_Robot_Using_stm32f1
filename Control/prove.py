import numpy as np
import cv2
cap=cv2.VideoCapture(0)
#trackbars
def nothing(x):
    pass
cv2.namedWindow("Trackbars")
cv2.createTrackbar('L-H','Trackbars',0,179,nothing)
cv2.createTrackbar('L-S','Trackbars',0,255,nothing)
cv2.createTrackbar('L-V','Trackbars',0,255,nothing)
cv2.createTrackbar('U-H','Trackbars',0,179,nothing)
cv2.createTrackbar('U-S','Trackbars',0,255,nothing)
cv2.createTrackbar('U-V','Trackbars',0,255,nothing)
cv2.setTrackbarPos('U-H','Trackbars',179)
cv2.setTrackbarPos('U-S','Trackbars',255)
cv2.setTrackbarPos('U-V','Trackbars',255)
font=cv2.FONT_HERSHEY_COMPLEX_SMALL
while True:
    ret,frame=cap.read()
    hsv_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    l_h=cv2.getTrackbarPos('L-H','Trackbars')
    l_s=cv2.getTrackbarPos('L-S','Trackbars')
    l_v=cv2.getTrackbarPos('L-V','Trackbars')
    u_h=cv2.getTrackbarPos('U-H','Trackbars')
    u_s=cv2.getTrackbarPos('U-S','Trackbars')
    u_v=cv2.getTrackbarPos('U-V','Trackbars')
    lower_color=np.array([l_h,l_s,l_v])#0,101,33
    upper_color=np.array([u_h,u_s,u_v])#31,255,255

    key=cv2.waitKey(1)
    if key==27:
        break
cap.release()
cv2.destroyAllWindows()
