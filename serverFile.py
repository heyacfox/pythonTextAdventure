from socket import *
import gameDirector
myHost = ''
myPort = 50007
sockobj = socket(AF_INET, SOCK_STREAM)
sockobj.bind((myHost, myPort))
sockobj.listen(5)


while True:
    connection, address = sockobj.accept()
    print('Server connected by', address)
    while True:
        data = connection.recv(1024)
        if not data: break
        mynewdata = gameDirector.interpretIncoming(bytes.decode(data))
        connection.send(b'Echo=>' + mynewdata)
    connection.close()


