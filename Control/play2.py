import serial
import time
from multiprocessing.connection import Listener
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
port="COM14" #This will be different for various devices and on windows it will probably be a COM port.
bluetooth=serial.Serial(port,9600)#Start communications with the bluetooth unit
print("Connected")
bluetooth.flushInput() 
PORT = 1233
server_sock = Listener(('localhost', PORT))
conn = server_sock.accept()
run = True
i=0
while run:
    x3cont= conn.recv()
    y3cont= conn.recv()
    i+=1
    #sending data to the other scripts
    #f=open("C://Users//hanan//Google Drive//P//Soccer Robot//Soccer_Robot_Using_stm32f1//Control//play3.txt","r")
    #s=f.read()
    #play=json.loads(s)
    #x3cont=play['3']['xcoord']
    #y3cont=play['3']['ycoord']
    #coords1 = pickle.load( open( "save3.p", "rb" ) )
    #x3cont=coords1['xcoord']
    #y3cont=coords1['ycoord']
    #print(x3cont)
    #print(y3cont)
    #time.sleep(1)
    #sending data to bluetooth
    sxcont=to_bin_and_string(x3cont)
    sycont=to_bin_and_string(y3cont)
    send1=str(x3cont)+' '+str(y3cont)
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
            sxcont=to_bin_and_string(x3cont)
            sycont=to_bin_and_string(y3cont)
            sender(sxcont)
            sender(sycont)
    prevdata=send
print("Done")
bluetooth.close()    
pygame.quit()