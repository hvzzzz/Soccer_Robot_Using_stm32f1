from multiprocessing.connection import Client
client = Client(('localhost', 1234))
run=True
while run:
    x=int(input('enter x: '))
    y=int(input('enter y: '))
    client.send(x)
    client.send(y)
#este script sends
