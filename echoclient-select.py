#!/usr/bin/env python

"""
An echo client that allows the user to send multiple lines to the server.
Entering a blank line will exit the client.
"""

#This code was found at http://ilab.cs.byu.edu/python/threadingmodule.html

import socket
import sys

host = 'localhost'
port = 50007
size = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))
sys.stdout.write('%')

while 1:
    # read from keyboard
    line = sys.stdin.readline()
    if line == '\n':
        break
    s.send(line)
    data = s.recv(size)
    sys.stdout.write(data)
    sys.stdout.write('%')
s.close()
