import message

class GameWorld():

    def __init__(self):
        self.list_of_users_dict = {}
        

    def receive_message(self, new_message):
        list_of_messages = []
        for u in self.list_of_users_dict.keys():
            sending_message = message.Message(
                "world", u, self.list_of_users_dict[u] +
                            ": New message sent by " +
                            self.list_of_users_dict[str(new_message.from_user_id)] +
                            ": " +
                            new_message.string_message)
            list_of_messages.append(sending_message)
        return list_of_messages

        
    
    def add_user(self, new_user_id):
        self.list_of_users_dict[str(new_user_id)] = "User" + str(len(self.list_of_users_dict))
        list_of_messages = []
        for u in self.list_of_users_dict.keys():
            sending_message = message.Message(
                "world", u, "A user " + self.list_of_users_dict[str(new_user_id)]
                            + " has entered the world")
            list_of_messages.append(sending_message)
        return list_of_messages
                
    def remove_user(self, user_id):
        self.list_of_users_dict.pop(str(user_id))
