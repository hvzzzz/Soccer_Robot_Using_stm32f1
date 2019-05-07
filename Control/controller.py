import pygame
import serial
import time
def to_bin_and_string(number):#returns a string containing the number in binay form 
    aans=''
    if number>0:
        ans=bin(number)
        aans=ans[2:]
        aans='0'+aans
    elif  number<0:
        ans=bin(number)
        aans=ans[2:]
        aans='1'+aans
    return aans
def sender(snumber):
    l=len(snumber)
    temporary=''
    for i in range(l):
        temporary=snumber[i]
        bluetooth.write(temporary.encode())
        #input_data=bluetooth.readline()
        #print(input_data.decode())
    bluetooth.write(' '.encode())
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
        #print (xcont)
        #bluetooth.write(str(xcont).encode())
    if keys[pygame.K_RIGHT]:
        x += vel
        xcont+=1
        if xcont>10:
            xcont=10
        #print (xcont)
        #bluetooth.write(str(xcont).encode())
    if keys[pygame.K_UP]:
        y -= vel
        ycont+=1
        if ycont>10:
            ycont=10
        #print (ycont)
        #bluetooth.write(str(ycont).encode())
    if keys[pygame.K_DOWN]:
        y += vel
        ycont-=1
        if ycont<-10:
            ycont=-10
        #print (ycont)
        #bluetooth.write(str(ycont).encode())
    #armamos el string que mandaremos al micro
    #sxcont=str(xcont)
    #sycont=str(ycont)
    sxcont=to_bin_and_string(xcont)
    sycont=to_bin_and_string(ycont)
    send=sxcont+' '+sycont
    #print(send)
    if i>1:
        if send!=prevdata:
            #bluetooth.write(sxcont.encode())
            #bluetooth.write(sycont.encode())
            sender(sxcont)
            sender(sycont)
            received=bluetooth.readline()
            print(received.decode())
            #print(send)
    prevdata=send
bluetooth.close() #Otherwise the connection will remain open until a timeout which ties up the /dev/thingamabob
print("Done")
#bluetooth.close()    
pygame.quit()