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
        #print(temporary)
        #print("\n")
        bluetooth.write(temporary.encode())
        #input_data=bluetooth.readline()
        #print(input_data.decode())
        #time.sleep(1)
    #print('3')
    #print("\n")
    bluetooth.write('3'.encode())
print("Start")
port="COM9" #This will be different for various devices and on windows it will probably be a COM port.
bluetooth=serial.Serial(port, 9600)#Start communications with the bluetooth unit
print("Connected")
#bluetooth.write(b"BOOP "+str.encode(str(i)))#These need to be bytes not unicode, plus a number
bluetooth.flushInput() #This gives the bluetooth a little kick
while True:
    #data=input()
    #bluetooth.write(data.encode())
    #input_data=bluetooth.readline()
    #print(input_data.decode())
    data=int(input())
    #temp=to_bin_and_string(data)
    #print(temp)
    #l=len(temp)
    #temporary=''
    for i in range(data):
        bluetooth.write('1'.encode())
        input_data=bluetooth.readline()
        print(input_data.decode())
    #    temporary=temp[i]
    #    print(temporary)
    #    print("\n")
        #bluetooth.write(temporary.encode())
        #print("pass0")
        #input_data=bluetooth.readline()
        #print(input_data.decode())
    #print("\n")
    #sender(temp)
    #bluetooth.write(temp.encode())
    #print("pass0")
    #input_data=bluetooth.readline()
    #print("pass1")
    #print(input_data.decode())
#for i in range(-10,11): #send 5 groups of data to the bluetooth
    #if (i%2==0):
        #temp='1 9'
        #print('pass1')
    #else:
        #temp='0 7'
        #print('pass2')
    #print('temp='+temp)
    #bluetooth.write(temp.encode(encoding="ascii",errors="ignore"))
    #print('pass4')
    #This reads the incoming data. In this particular example it will be the "Hello from Blue" line
    #print(type(input_data))
    #print('pass5')
    #These are bytes coming in so a decode is needed
    #print('pass6')
    #time.sleep(1) #A pause between bursts
bluetooth.close() #Otherwise the connection will remain open until a timeout which ties up the /dev/thingamabob
print("Done")
