import pygame
import serial
import time
def pressed(prev,new):
    if prev==new:
        return False
    else:
        return True
def to_bin_and_string(number):
    aans=''
    if number>0:
        ans=bin(number)
        aans=ans[2:]
        aans='0'+aans
    elif  number<0:
        ans=bin(number)
        aans=ans[3:]
        aans='1'+aans
    else:
        aans='0'+'0'
    return aans
def sender(snumber):
    l=len(snumber)
    temporary=''
    for i in range(l):
        temporary=snumber[i]
        bluetooth.write(temporary.encode())
    bluetooth.write('3'.encode())
def sender1(snumber):
    l=len(snumber)
    temporary=''
    for i in range(l):
        temporary=snumber[i]
        bluetooth1.write(temporary.encode())
    bluetooth1.write('3'.encode())
def sender2(snumber):
    l=len(snumber)
    temporary=''
    for i in range(l):
        temporary=snumber[i]
        bluetooth2.write(temporary.encode())
    bluetooth2.write('3'.encode())
pygame.init()
win = pygame.display.set_mode((500,10))
pygame.display.set_caption("First Game")
#port="COM4"
port1="COM4"
#port2="COM7" #This will be different for various devices and on windows it will probably be a COM port.
#bluetooth=serial.Serial(port,9600)
bluetooth1=serial.Serial(port1,9600)#Start communications with the bluetooth unit
#bluetooth2=serial.Serial(port2,9600)
print("Connected")
#bluetooth.flushInput()
bluetooth1.flushInput()
#bluetooth2.flushInput()    
x = 50
x1cont,x2cont,x3cont,x1send,x2send,x3send=0,0,0,0,0,0
y = 50
y1cont,y2cont,y3cont,y1send,y2send,y3send=0,0,0,0,0,0
vel = 5
run = True
sendnew,sendnew1,sendnew2,send1,send2,send3,prevdata1,prevdata2,prevdata3=0,0,0,0,0,0,0,0,0
i=0
while run:
    i+=1
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        run=False
    #first player
    if keys[pygame.K_KP4]:
        x1cont-=1
        time.sleep(0.01)
    if keys[pygame.K_KP6]:
        x1cont+=1
        time.sleep(0.01)
    if keys[pygame.K_KP8]:
        y1cont-=1
        time.sleep(0.01)
    if keys[pygame.K_KP3]:
        y1cont+=1
        time.sleep(0.01)
    #second player
    if keys[pygame.K_d]:
        time.sleep(0.01)
        x2cont+=1
    if keys[pygame.K_a]:
        x2cont-=1
        time.sleep(0.01)
    if keys[pygame.K_w]:
        y2cont-=1
        time.sleep(0.01)
    if keys[pygame.K_s]:
        y2cont+=1
        time.sleep(0.01)
    #third player
    if keys[pygame.K_j]:
        time.sleep(0.01)
        x3cont-=1
    if keys[pygame.K_l]:
        x3cont+=1
        time.sleep(0.01)
    if keys[pygame.K_i]:
        y3cont-=1
        time.sleep(0.01)
    if keys[pygame.K_k]:
        y3cont+=1
        time.sleep(0.01)
    sendnew=str(x1cont)+' '+str(y1cont)#contiene la informacion original de las teclas
    sendnew1=str(x2cont)+' '+str(y2cont)#contiene la informacion original de las teclas
    sendnew2=str(x3cont)+' '+str(y3cont)#contiene la informacion original de las teclas
    if i>1:
        if x1cont<=10 and x1cont>=-10:
            if pressed(sendnew,prevdata1):
                x1send=x1cont
            else:
                x1send=0
                x1cont=0
        if x1cont>10:
            if pressed(sendnew,prevdata1):
                x1send=10
            else:
                x1send=0
                x1cont=0
        if x1cont<-10:
            if pressed(sendnew,prevdata1):
                x1send=-10
            else:
                x1send=0
                x1cont=0
        if y1cont<=10 and y1cont>=-10:
            if pressed(sendnew,prevdata1):
                y1send=y1cont
            else:
                y1send=0
                y1cont=0
        if y1cont>10:
            if pressed(sendnew,prevdata1):
                y1send=10
            else:
                y1send=0
                y1cont=0
        if y1cont<-10:
            if pressed(sendnew,prevdata1):
                y1send=-10
            else:
                y1send=0
                y1cont=0
#second player
        if x2cont<=10 and x2cont>=-10:
            if pressed(sendnew1,prevdata2):
                x2send=x2cont
            else:
                x2send=0
                x2cont=0
        if x2cont>10:
            if pressed(sendnew1,prevdata2):
                x2send=10
            else:
                x2send=0
                x2cont=0
        if x2cont<-10:
            if pressed(sendnew1,prevdata2):
                x2send=-10
            else:
                x2send=0
                x2cont=0
        if y2cont<=10 and y2cont>=-10:
            if pressed(sendnew1,prevdata2):
                y2send=y2cont
            else:
                y2send=0
                y2cont=0
        if y2cont>10:
            if pressed(sendnew1,prevdata2):
                y2send=10
            else:
                y2send=0
                y2cont=0
        if y2cont<-10:
            if pressed(sendnew1,prevdata2):
                y2send=-10
            else:
                y2send=0
                y2cont=0
#thrid player
        if x3cont<=10 and x3cont>=-10:
            if pressed(sendnew2,prevdata3):
                x3send=x3cont
            else:
                x3send=0
                x3cont=0
        if x3cont>10:
            if pressed(sendnew2,prevdata3):
                x3send=10
            else:
                x3send=0
                x3cont=0
        if x3cont<-10:
            if pressed(sendnew2,prevdata3):
                x3send=-10
            else:
                x3send=0
                x3cont=0
        if y3cont<=10 and y3cont>=-10:
            if pressed(sendnew2,prevdata3):
                y3send=y3cont
            else:
                y3send=0
                y3cont=0
        if y3cont>10:
            if pressed(sendnew2,prevdata3):
                y3send=10
            else:
                y3send=0
                y3cont=0
        if y3cont<-10:
            if pressed(sendnew2,prevdata3):
                y3send=-10
            else:
                y3send=0
                y3cont=0
        sxcont1=to_bin_and_string(x1send)
        sycont1=to_bin_and_string(y1send)
        sxcont2=to_bin_and_string(x2send)
        sycont2=to_bin_and_string(y2send)
        sxcont3=to_bin_and_string(x3send)
        sycont3=to_bin_and_string(y3send)
        send1=str(x1send)+' '+str(y1send)#dato a mandar,esta en los limites de -10 a 10
        sendnew=str(x1cont)+' '+str(y1cont)#dato que contiene la informacion original
        print(send1)
        send2=str(x2send)+' '+str(y2send)#dato a mandar,esta en los limites de -10 a 10
        sendnew1=str(x2cont)+' '+str(y2cont)#dato que contiene la informacion original
        #print(send2)
        send3=str(x3send)+' '+str(y3send)#dato a mandar,esta en los limites de -10 a 10
        sendnew2=str(x3cont)+' '+str(y3cont)#dato que contiene la informacion original
        #print(send3)
        #sender(sxcont1)
        #sender(sycont1)
        sender1(sxcont2)
        sender1(sycont2)
        #sender2(sxcont3)
        #sender2(sycont3)
    prevdata1=sendnew
    prevdata2=sendnew1
    prevdata3=sendnew2
print("Done")
#bluetooth.close()
bluetooth1.close()    
#bluetooth2.close()        
pygame.quit()