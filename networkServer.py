import gameWorldInterface
import threading
import select
import socket
import sys
import message
import select

myHost = ''
myPort = 50007

global idToAddress
idToAddress = {}
global addressToId
addressToId = {}

#Note: This website is cool http://ilab.cs.byu.edu/python/threadingmodule.html

class Server:
    def __init__(self, newGameWorldInterface):
        self.host = ''
        self.port = 50007
        self.backlog = 5
        self.size = 1024
        self.server = None
        self.threads = []
        #This variable is a dictionary so we know which client to send
        #messages to when we get them from game world
        #Where does this get called.
        self.gameWorldInterface = newGameWorldInterface

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
            c = Client(self.server.accept(), self.gameWorldInterface)
            c.start()
            #This starts the thread which is above what we do
            self.threads.append(c)
            print("Added Client:" + str(c.address))
            #Then we append it to our threads list
            #Here's some more things
            #we add the ids and the address to our dictionaries for use later
            #THIS CAN'T WORK BECAUSE CLIENTS OPERATE INDEPENDENTLY UGH...
            global idToAddress
            global addressToId
            idToAddress[str(c.address)] = str(c.address)
            addressToId[str(c.address)] = str(c.address)
            """
            if len(self.gameWorldInterface.waitingMessagesToServer) > 0:
                #sends the whole mess of messages to all the clients
                for m in gameWorldInterface.waitingMessageToServer:
                    for t in threads:
                        if t.address == m.toUserId:
                            t.send(m.stringMessage.encode('UTF-8'))
            """
                            
#hacking code from here now: https://docs.python.org/3/howto/sockets.html
class Client(threading.Thread):
    def __init__(self, clienttuplething, gameWorldInter):
        #we can now use self.myconnection to send things back to server
        threading.Thread.__init__(self)
        self.client = clienttuplething[0]
        self.address = clienttuplething[1]
        self.size = 1024
        self.gameWorldInterface = gameWorldInter

    def run(self):
        running = 1
        while running:
            self.client.setblocking(0)
            ready = select.select([self.client], [], [], 5)
            if ready[0]:
                data = self.client.recv(self.size)
            #we receive data constantly through the receive socket
                if data:
                    #if we find something
                    #we need two options. If we get a message from a client,
                    #we pass it to the gameWorld and it can figure it out.
                    #If we get a message from the gameWorld???
                    #self.client.send(data)
                    global addressToId
                    print("We got: " + data.decode('UTF-8') + " from " + str(self.address))
                    #we send it back?
                    #NO, instead, let's add it to our interfacer.
                    self.sendData(addressToId[str(self.address)], data.decode('UTF-8'))
                else:
                    self.client.close()
                    running = 0
                    #ELSE WE JUST DIE WHY???
            print("Haven't gotten anything in a while")
            messagesWaiting = self.gameWorldInterface.receiveMessagesToServerToClient(str(self.address))
            if len(messagesWaiting) > 0:
                for m in messagesWaiting:
                    self.client.send(m.stringMessage)
                
                    
    def sendData(self, clientId, dataAsString):
        newMessage = message.Message(clientId, "GameWorld", dataAsString)
        self.gameWorldInterface.sendMessageToWorld(newMessage)

#if __name__ == "__main__":
#    s = Server()
#    s.run()
