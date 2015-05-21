#!/usr/bin/env python

"""
An echo client that allows the user to send multiple lines to the server.
Entering a blank line will exit the client.
"""

#This code was found at http://ilab.cs.byu.edu/python/threadingmodule.html

#taking some code from http://bytes.com/topic/python/answers/43936-canceling-interrupting-raw_input

import socket
import sys
import threading
from threading import Thread
import select
import time
import msvcrt
import string
import selectors

host = 'localhost'
port = 50007
size = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))
s.setblocking(0)
#sys.stdout.write('%')
"""
while :1
    # read from keyboard
    line = input("What do you do?\n>> ").encode('UTF-8')
    if line == '\n':
        break
    s.send(line)
    data = s.recv(size)
    sys.stdout.write(data.decode('UTF-8'))
    sys.stdout.write('%>> ')
s.close()
"""

#https://docs.python.org/3/library/selectors.html
#maybe that will help I don't know


class receiveLoop(threading.Thread):
    def __init__(self):
        self.run()

    def run(self):
        prompt()
        while 1:
            #ready = select.select([s], [], [], 5)
            read_sockets = select.select([sys.stdin, s], [], [])
            for sock in read_sockets[0]:
                if sock == s:
                    data = sock.recv(size)
                    if not data:
                        print("YOU BROKE IT")
                    else:
                        print("WE GOT DATA")
                else:
                    msg = sys.stdin.readline()
                    s.send(msg)
                    prompt()
            #print("We never hit ready")
            #inputLoop()

def inputLoop():
    line=input("What do you do?\n>> ").encode('UTF-8')
    s.send(line)

class inputLooping(threading.Thread):
    def __init__(self):
        self.run()

        def run(self):
            line=input("What do you do?\n>> ").encode('UTF-8')
            s.send(line)




def read(conn, mask):
    data = conn.recv(size)
    if data:
        print("YO")
    else:
        print("Um that's not a thing")

def acceptInternet(sock, mask):
    print("Just got an internet message")

def acceptStdInput(sock, mask):
    print("I just got std input")

sel = selectors.DefaultSelector()
sys.stdin.flush()

sel.register(s, selectors.EVENT_READ, acceptInternet)
sel.register(sys.stdout, selectors.EVENT_READ, acceptStdInput)

while True:
    events = sel.select()
    for key, mask in events:
        callback = key.data
        

#ONE LINE, CALL THE FUNCTION TO SEND MESSAGES
def sendMessage(TextMessage):
    s.send(TextMessage.encode('UTF-8'))
#inputLoop()
#inputLoop()
#myreceivethread = receiveLoop()
#myreceivethread.start()
#myinputthread = inputLooping()
#myinputthread.start()
