import sys
from socket import *
serverHost = 'localhost'
serverPort = 50007

message = [b'Hello network World']

if len(sys.argv) > 1:
    serverHost = sys.argv[1]
    if len(sys.argv) > 2:
        message = (x.encode() for x in sys.argv[2:])

#sockobj = socket(AF_INET, SOCK_STREAM)
#sockobj.connect((serverHost, serverPort))

#This function requires you to submit it as a byte text, such as the
#'message' up there
def sendmessage(mytext):
    sockobj = socket(AF_INET, SOCK_STREAM)
    sockobj.connect((serverHost, serverPort))
    for line in mytext:
        sockobj.send(line)
        data = sockobj.recv(1024)
        print('Client received:', data)
    sockobj.close()

#This function can take in strings and sends the messages out
def sendmsg(mystrtext):
    mybytetext = mystrtext.encode('UTF-8')
    mylinedbytetext = []
    mylinedbytetext.append(mybytetext)
    sockobj = socket(AF_INET, SOCK_STREAM)
    sockobj.connect((serverHost, serverPort))
    for line in mylinedbytetext:
        sockobj.send(line)
        data = sockobj.recv(1024)
        print('Client received:', data.decode('UTF-8'))
    sockobj.close()

