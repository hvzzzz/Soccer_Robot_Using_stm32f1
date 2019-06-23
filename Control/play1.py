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
port="COM12" #This will be different for various devices and on windows it will probably be a COM port.
bluetooth=serial.Serial(port,9600)#Start communications with the bluetooth unit
print("Connected")
bluetooth.flushInput() 
PORT = 1234
server_sock = Listener(('localhost', PORT))
conn = server_sock.accept()
run = True
i=0
while run:
    x2cont= conn.recv()
    y2cont= conn.recv()
    i+=1
    #sending data to the other scripts
    #f=open("C://Users//hanan//Google Drive//P//Soccer Robot//Soccer_Robot_Using_stm32f1//Control//play2.txt","r")
    #s=f.read()
    #play=json.loads(s)
    #x2cont=play['2']['xcoord']
    #y2cont=play['2']['ycoord']
    #coords = pickle.load( open( "save.p", "rb" ) )
    #x2cont=coords['xcoord']
    #y2cont=coords['ycoord']
    #print(type(x2cont))
    #print(type(y2cont))
    #time.sleep(1)
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