import serial
import time
print("Start")
port="COM9" #This will be different for various devices and on windows it will probably be a COM port.
bluetooth=serial.Serial(port, 9600)#Start communications with the bluetooth unit
print("Connected")
#bluetooth.write(b"BOOP "+str.encode(str(i)))#These need to be bytes not unicode, plus a number
bluetooth.flushInput() #This gives the bluetooth a little kick
for i in range(10): #send 5 groups of data to the bluetooth
	#print("Ping")
    temp=0
    if (i%2==0):
        temp='0'
    else:
        temp='1'
    bluetooth.write(temp.encode())
    input_data=bluetooth.readline()#This reads the incoming data. In this particular example it will be the "Hello from Blue" line
    print(input_data.decode())#These are bytes coming in so a decode is needed
    time.sleep(1) #A pause between bursts
bluetooth.write('2'.encode())
bluetooth.close() #Otherwise the connection will remain open until a timeout which ties up the /dev/thingamabob
print("Done")
