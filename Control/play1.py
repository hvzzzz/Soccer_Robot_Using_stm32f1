import pygame
import serial
import time
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
pygame.init()
win = pygame.display.set_mode((500,10))
pygame.display.set_caption("First Game")
port="COM9" #This will be different for various devices and on windows it will probably be a COM port.
bluetooth=serial.Serial(port,9600)#Start communications with the bluetooth unit
print("Connected")
bluetooth.flushInput() 
x = 50
x1cont=0
x2cont=0
x3cont=0
y = 50
y1cont=0
y2cont=0
y3cont=0
vel = 5
run = True
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
    if keys[pygame.K_LEFT]:
        x -= vel
        x1cont-=1
        if x1cont<-10:
            x1cont=-10
    if keys[pygame.K_RIGHT]:
        x += vel
        x1cont+=1
        if x1cont>10:
            x1cont=10
    if keys[pygame.K_UP]:
        y -= vel
        y1cont+=1
        if y1cont>10:
            y1cont=10
    if keys[pygame.K_DOWN]:
        y += vel
        y1cont-=1
        if y1cont<-10:
            y1cont=-10
    #second player
    if keys[pygame.K_a]:
        x -= vel
        x2cont-=1
        if x2cont<-10:
            x2cont=-10
    if keys[pygame.K_d]:
        x += vel
        x2cont+=1
        if x2cont>10:
            x2cont=10
    if keys[pygame.K_w]:
        y -= vel
        y2cont+=1
        if y2cont>10:
            y2cont=10
    if keys[pygame.K_s]:
        y += vel
        y2cont-=1
        if y2cont<-10:
            y2cont=-10
    #third player
    if keys[pygame.K_j]:
        x -= vel
        x3cont-=1
        if x3cont<-10:
            x3cont=-10
    if keys[pygame.K_l]:
        x += vel
        x3cont+=1
        if x3cont>10:
            x3cont=10
    if keys[pygame.K_i]:
        y -= vel
        y3cont+=1
        if y3cont>10:
            y3cont=10
    if keys[pygame.K_k]:
        y += vel
        y3cont-=1
        if y3cont<-10:
            y3cont=-10
    #sending data to the other scripts
    
    #sending data to bluetooth
    sxcont=to_bin_and_string(x2cont)
    sycont=to_bin_and_string(y2cont)
    send1=str(x2cont)+' '+str(y2cont)
    send=sxcont+' '+sycont
    if i>1:
        if send!=prevdata:
            sender(sxcont)
            sender(sycont)
            print(send1)
            #received=bluetooth.readline()
            #print(received.decode())
        else:
            x2cont=0;
            y2cont=0;
            sxcont=to_bin_and_string(x2cont)
            sycont=to_bin_and_string(y2cont)
            sender(sxcont)
            sender(sycont)
    prevdata=send
print("Done")
bluetooth.close()    
pygame.quit()