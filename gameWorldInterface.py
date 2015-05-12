#This class will take messages from the game and give them to the server,
#as well as take messages from the server and give them to the
#game. Messages coming from the server will ALWAYS be client messages,
#while messages coming from the game world will ALWAYS be game world messages

#Since I can't control how messages come in, I just put them in a list
#When the other people are ready to handle them, they call the
#respective receive messages function to get the messages they need to handle

class gameWorldInterface:

    def __init__(self):
        self.waitingMessagesToServer = []
        self.waitingMessagesToWorld = []

    def sendMessageToServer(self, newMessage):
        self.waitingMessagesToServer.append(newMessage)
        #This function takes in a message and sends it to the server

    def sendMessageToWorld(self, newMessage):
        self.waitingMessagesToWorld.apend(newMessage)

    #returns a list of messages, in time sequence order from oldest to most recent
    def receiveMessagesToWorld(self):
        #once you've confirmed there are messages to receive, calling
        #this function will return the messages meant for the game world
        tempMessages = self.waitingMessagesToWorld
        self.waitingMessagesToWorld = []
        return tempMessages

    def receiveMessagesToServer(self):
        #Once you've confirmed there are messages to receive, calling
        #this function will return the messages meant for the server
        tempMessages = self.waitingMessages
        self.waitingMessages = []
        return tempMessages

    def receiveMessagesToServerToClient(self, clientId):
        tempMessages = []
        tempReturnMessages = []
        for m in self.waitingMessagesToServer:
            if m.clientId == clientId:
                tempReturnMessages.append(m)
            else:
                tempMessages.append(m)
        self.waitingMessagesToServer = tempMessages
        return tempReturnMessages
