#This class defines the messages that
#get sent from the client to the server,
#and from the server to the client.

#My job is to send things. It's everyone else's
#problem to see what comes out of it

#Note: Because python, the message can literally be anything.
#I can take it objects if we want, but currently
#I will only plan to handle string messages.

#I don't know what the Id system we want to use looks like yet.
#Whatever we choose, server has to convert it to port addresses anyway

class Message:

    def __init__(self, newFromUserId, newToUserId, newMessage):
        self.fromUserId = newFromUserId
        self.toUserId = newToUserId
        self.stringMessage = newMessage
        
