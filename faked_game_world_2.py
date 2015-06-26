import message

class GameWorld():

    def __init__(self):
        #there is no data I guess
        self.user_list = ""
        self.other_things = ""

    #This MUST return a list of messages and the people they should go to
    def receive_message(self, somemessage):
        returningmessages = []
        messagestring = somemessage.stringMessage
        for x in self.user_list:
            returningmessages.append(message.Message("world", x, str(x) + ": someone said" + messagestring))
        return returningmessages
            
            
            
