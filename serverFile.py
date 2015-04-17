#from socket import *
import gameDirector
import threading
import select
import socket
import sys

myHost = ''
myPort = 50007
"""
#sockobj = socket(AF_INET, SOCK_STREAM)
#sockobj.bind((myHost, myPort))
#sockobj.listen(5)


#Note: This website is cool http://ilab.cs.byu.edu/python/threadingmodule.html

#listOfUsers = []

#running this function will start up the server. The server will run
#for infinity
def serverGo():
    while True:
        connection, address = sockobj.accept()
        print('Server connected by', address)
        #after we have the client, we pass them into the client
        #receiving loop
        clientLoop(connection, address)
        while True:
            data = connection.recv(1024)
            if not data: break
            #pass the data off to a different function with the address
            interpretClientInput(bytes.decode(data), address, connection)
            #connection.send(b'Echo=>' + mynewdata)
        connection.close()


#This function interprets the data from a client
def interpretClientInput(decodedInput, address, connection):

#when we get a connection, we need to get that user to give us their username


#Then, when they log in again the next time, we ask them who they are


#This function loops the client once they have been connected
def clientLoop(connection, address):
    while True:
        data = connection.recv(1024)
"""
"""
#This class below is based on the code at the URL in the comments at the top
#It is a multi-client way of doing servers
class Server:
    def __init__(self):
        self.host = ''
        self.port = 50007
        self.backlog = 5
        self.size = 1024
        self.server = None
        self.threads = []

    def open_socket(self):
        try:
            self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server.bind((self.host, self.port))
            self.server.listen(5)
        except socket.error:
            if self.server:
                self.server.close()
            print("Could not open socket: ")
            sys.exit(1)
    def run(self):
        self.open_socket()
        myinput = [self.server, sys.stdin]
        running = 1
        while running:
            inputready, outputready, exceptready = select.select(myinput, [], [])

            for s in inputready:
                if s == self.server:
                    c = Client(self.server.accept())
                    c.start()
                    #we append to our threads in this object for
                    #every client that we start
                    self.threads.append(c)

                elif s == sys.stdin:
                    #but if we get regular system input
                    junk = sys.stdin.readline()
                    running = 0
                    #we...give up?

        self.server.close()
        for c in self.threads:
            c.join()

class Client(threading.Thread):
    def __init__(self, client, address):
        threading.Thread.__init__(self)
        self.client = client
        self.address = address
        self.size = 1024

    def run(self):
        running = 1
        while running:
            data = self.client.recv(self.size)
            if data:
                self.client.send(data)
            else:
                self.client.close()
                running = 0
if __name__ == "__main__":
    s = Server()
    s.run()
"""
#The above doesn't actually work for some reason relating to it being pythong 2.7ish

class Server:
    def __init__(self):
        self.host = ''
        self.port = 50007
        self.backlog = 5
        self.size = 1024
        self.server = None
        self.threads = []

    def open_socket(self):
        try:
            self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server.bind((self.host,self.port))
            self.server.listen(5)
            #we just opened up 50007...I think. It's listening for stuff now
        except socket.error:
            if self.server:
                self.server.close()
            print("Can't open that socket")
            sys.exit(1)
                
    def run(self):
        self.open_socket()
        #we just opened a socket. Now we want to...listen for inputs?
        running = 1
        while running:
            c = Client(self.server.accept())
            c.start()
            #This starts the thread which is above what we do
            self.threads.append(c)
            #Then we append it to our threads list
        #hacking code from here now: https://docs.python.org/3/howto/sockets.html


    def acceptClients(self):
        #Running this function will create an infinite loop of accepting
        #clients, but I want to READ data from clients too!!!
        while True:
            print("X")
                


class Client(threading.Thread):
    def __init__(self, clienttuplething ):
        #we can now use self.myconnection to send things back to server
        threading.Thread.__init__(self)
        self.client = clienttuplething[0]
        self.address = clienttuplething[1]
        self.size = 1024

    def run(self):
        running = 1
        while running:
            data = self.client.recv(self.size)
            #we receive data constantly through the receive socket
            if data:
                #if we find something
                self.client.send(data)
                print("We got: " + data.decode('UTF-8') + " from " + str(self.address))
                #we send it back?
            else:
                self.client.close()
                running = 0
                #ELSE WE JUST DIE WHY???

if __name__ == "__main__":
    s = Server()
    s.run()
