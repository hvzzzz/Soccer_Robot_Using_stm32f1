from multiprocessing.connection import Listener
PORT = 1234
server_sock = Listener(('localhost', PORT))
conn = server_sock.accept()
run =True
while run:
    x = conn.recv()
    y = conn.recv()
    x+=1
    y+=1
    print(type(x))
    print(type(y))
#este script recive
