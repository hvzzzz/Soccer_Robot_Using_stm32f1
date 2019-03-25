import numpy as np
import cv2
cap=cv2.VideoCapture(0)
#trackbars
def nothing(x):
    pass
cv2.namedWindow("Trackbars")
cv2.createTrackbar("L-H","Trackbars",0,179,nothing)
cv2.createTrackbar("L-S","Trackbars",0,255,nothing)
cv2.createTrackbar("L-V","Trackbars",0,255,nothing)
cv2.createTrackbar("U-H","Trackbars",179,179,nothing)
cv2.createTrackbar("U-S","Trackbars",255,255,nothing)
cv2.createTrackbar("U-V","Trackbars",255,255,nothing)
font=cv2.FONT_HERSHEY_COMPLEX_SMALL
while True:
    ret,frame=cap.read()
    hsv_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    l_h=cv2.getTrackbarPos("L-H","Trackbars")
    l_s=cv2.getTrackbarPos("L-S","Trackbars")
    l_v=cv2.getTrackbarPos("L-V","Trackbars")
    u_h=cv2.getTrackbarPos("U-H","Trackbars")
    u_s=cv2.getTrackbarPos("U-S","Trackbars")
    u_v=cv2.getTrackbarPos("U-V","Trackbars")
    #lower_color=np.array([l_h,l_s,l_v])#0,101,33
    #upper_color=np.array([u_h,u_s,u_v])#31,255,255
    lower_color=np.array([125,8,118])#0,147,31
    upper_color=np.array([179,44,255])#18,236,255
    mask=cv2.inRange(hsv_frame,lower_color,upper_color)
    kernel=np.ones((5,5),np.uint8)
    mask=cv2.erode(mask,kernel)
    #contours detection
    contours, hierarchy=cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for i in contours:
        area=cv2.contourArea(i)
        approx=cv2.approxPolyDP(i,0.02*cv2.arcLength(i,True),True)
        x=approx.ravel()[0]
        y=approx.ravel()[1]
        if area >400:
            cv2.drawContours(frame,[approx],0,(0,0,0),3)
            if len(approx)==4:
                cv2.putText(frame,"Rectangle",(x,y),font,1,(0,0,0))
            if 10<len(approx)<20:
                cv2.putText(frame,"Circle",(x,y),font,1,(0,0,0))
        #print(len(i))
    #result=cv2.bitwise_and(frame,frame,mask=mask)
    cv2.imshow("frame",frame)
    cv2.imshow("mask",mask)
    #cv2.imshow("result",result)
    key=cv2.waitKey(1)
    if key==27:
        break
cap.release()
cv2.destroyAllWindows()
