import sys
from socket import *
serverHost = '52.10.105.147'
serverPort = 50007

message = [b'Hello network World']

if len(sys.argv) > 1:
    serverHost = sys.argv[1]
    if len(sys.argv) > 2:
        message = (x.encode() for x in sys.argv[2:])

#sockobj = socket(AF_INET, SOCK_STREAM)
#sockobj.connect((serverHost, serverPort))

def sendmessage(mytext):
    sockobj = socket(AF_INET, SOCK_STREAM)
    sockobj.connect((serverHost, serverPort))
    for line in mytext:
        sockobj.send(line)
        data = sockobj.recv(1024)
        print('Client received:', data)
    sockobj.close()

