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

host = 'localhost'
port = 50007
size = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))
sys.stdout.write('%')
"""
while 1:
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
class receiveLoop(threading.Thread):
    def __init__(self):
        self.run()

    def run(self):
        while 1:
            data = s.recv(size)
            if data:
                sys.stdout.write(data.decode('UTF-8'))

def inputLoop():
    while 1:
        line=input("What do you do?\n>> ").encode('UTF-8')
        s.send(line)

#mythread = receiveLoop()
#receiveLoop.start()


inputLoop()
