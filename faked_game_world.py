import gameWorldInterface
import time
import random
import message
import threading


class FakeWorld(threading.Thread):
    randomwords = ['Hey', 'Why', 'You There?', 'I care']

    def __init__(self, gwi):
        threading.Thread.__init__(self)
        self.Interface = gwi
        self.list_of_peeps = ["Kyle"]
        self.list_of_received_messages = []

    def run(self):
        #This is the primary loop this code uses
        while True:
            time.sleep(3)
            self.give_user_message(random.choice(self.list_of_peeps), random.choice(self.randomwords))
            self.get_new_messages()


    def get_new_messages(self):
        #Gets new messages from the game world interface, sticks
        #them in the list of received messages
        while self.Interface.has_to_game_world_messages():
            self.list_of_received_messages.append(self.Interface.to_game_world_one_message())
            
        
        
    def give_user_message(self, someuser, someword):
        #Gives a user in the listofpeeps a random message
        newMessage = message.Message("World", someuser, someword)
        self.Interface.sendMessageToServer(newMessage)
        
