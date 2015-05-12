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

host = 'localhost'
port = 50007
size = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))
s.setblocking(0)
sys.stdout.write('%')
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
class receiveLoop(threading.Thread):
    def __init__(self):
        self.run()

    def run(self):
        while 1:
            ready = select.select([s], [], [], 5)
            if ready[0]: 
                data = s.recv(size)
                if data:
                    sys.stdout.write(data.decode('UTF-8'))
                else:
                    print("No data received")
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

#inputLoop()
#inputLoop()
#myreceivethread = receiveLoop()
#myreceivethread.start()
#myinputthread = inputLooping()
#myinputthread.start()

#Oh my gosh what is happening here: http://stackoverflow.com/questions/2408560/python-nonblocking-console-input
"""
def add_input(input_queue):
    while True:
        input_queue.put(sys.stdin.read(1))

def myfunction():
    input_queue = Queue.Queue()

    input_thread = threading.Thread(target=add_input, args=(input_queue,))
    input_thread.daemon = True
    input_thread.start()

    last_update = time.time()
    while True:

        if time.time()-last_update>0.5:
            sys.stdout.write(".")
            last_update = time.time()

        if not input_queue.empty():
            print("\ninput:" +  input_queue.get())
            
myfunction()
"""

#WHAT DOES THAT EVEN MEAN LION: http://code.activestate.com/recipes/531824-chat-server-client-using-selectselect/

def cmdloop():
    flag = False
    while not flag:
        try:
            sys.stdout.write("Type Something")
            sys.stdout.flush()

            inputready, outputready, exceptrdy = select.select([0, s], [], [])

            for i in inputready:
                if i == 0:
                    data = sys.stdin.readline().strip()
                    if data:
                        s.send(data.encode('UTF-8'))
                elif i == s:
                    data = s.recv(size)
                    if not data:
                        print("WHAT DOES THAT")
                        flag = True
                        break
                    else:
                        sys.stdout.write(data.decode('UTF-8') + '\n')
                        sys.stdout.flush()
        except RuntimeError:
            print("EVEN MEAN LION")
            s.close()
            break

cmdloop()

#I don't know what this means but it sounds important: https://docs.python.org/3.4/library/selectors.html#module-selectors

                    
