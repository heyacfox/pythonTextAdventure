#This class defines the messages that
#get sent from the client to the server,
#and from the server to the client.

#I don't know what the Id system we want to use looks like yet.
#Whatever we choose, server has to convert it to port addresses anyway

class Message:

    def __init__(self, new_from_user_id, new_to_user_id, new_message):
        #A string: Who the message was sent from. Can be a user id,
        #but is also often "server" or "world". 
        self.from_user_id = new_from_user_id
        #The intended recipient of the message. Can be a user id, but can
        #also be "server" or "world". Use "server" when sending from the
        #world to indicate a system message, and use "world" when sending
        #from the server to indicate that a user typed in something
        #that was not specifically directed towards anyone.
        self.to_user_id = new_to_user_id
        #The string content of the message
        self.string_message = new_message
        
