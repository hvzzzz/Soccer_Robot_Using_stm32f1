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
xcont=0
y = 50
ycont=0
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
    if keys[pygame.K_LEFT]:
        x -= vel
        xcont-=1
        if xcont<-10:
            xcont=-10
    if keys[pygame.K_RIGHT]:
        x += vel
        xcont+=1
        if xcont>10:
            xcont=10
    if keys[pygame.K_UP]:
        y -= vel
        ycont+=1
        if ycont>10:
            ycont=10
    if keys[pygame.K_DOWN]:
        y += vel
        ycont-=1
        if ycont<-10:
            ycont=-10
    sxcont=to_bin_and_string(xcont)
    sycont=to_bin_and_string(ycont)
    send1=str(xcont)+' '+str(ycont)
    send=sxcont+' '+sycont
    if i>1:
        if send!=prevdata:
            sender(sxcont)
            sender(sycont)
            print(send1)
            #received=bluetooth.readline()
            #print(received.decode())
    prevdata=send
print("Done")
bluetooth.close()    
pygame.quit()