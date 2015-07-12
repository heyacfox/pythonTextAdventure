#Lots of code blatantly stolen from the Websocket demo included with
#Tornado

import tornado.ioloop
import tornado.web
import tornado.options
import tornado.web
import tornado.websocket
import os.path
import uuid
from tornado import gen
import message

#I am storing the GameWorld in a global because I am a terrible programmer
#but also because I don't know how to pass the variable on a socket connection
#because I have no idea how sockets are

global GAME_WORLD
GAME_WORLD = ""
#WAIT CAN I JUST PASS A TICK INTO THE WORLD EVERY SECOND?
#Every second, time out of waiting for messages and tick the world, then
#wait for messages again


#The application handles
class Application(tornado.web.Application):
    def __init__(self):
        #The handlers are all the "subpages" you can get to
        #while the server is active. Going to one of those
        #sub pages will activate a function
        handlers = [
            (r"/", MainHandler),
            #passing the game world into EACH SOCKET when it gets...made?...I'm not sure what's happening here
            #Oh yeah, this is called from the JavaScript in the index.html like whaaaaaaat
            (r"/ComSocket", ComSocket),
            (r"/ENDTHIS", EndLoop),
        ]
        #These are settings for the application
        settings = dict(
            #The templates are where the HTML files are stored. So you call HTML files like whaaaaat
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            #Static is where the JS files are stored. I don't know why they're stored in two seperate places
            static_path=os.path.join(os.path.dirname(__file__), "static"),
        )
        
        tornado.web.Application.__init__(self, handlers, **settings)

#This class is what gets hit when the user finds the default page.
class MainHandler(tornado.web.RequestHandler):
    #@tornado.web.authenticated
    def get(self):
        #Render creates a webpage. And it does something with messages?...not sure what that means
        self.render("index.html", messages=ComSocket.cache)
        print(repr(self.request))

#I made this functon. When this function gets called the world ends. I mean the server
class EndLoop(tornado.web.RequestHandler):
    def get(self):
        tornado.ioloop.IOLoop.instance().stop()
        print("Heysup this is end")

#OH MY GOSH I JUST DON'T KNOW WHAT'S HAPPENING HERE
class ComSocket(tornado.websocket.WebSocketHandler):
    #OOOOOH ALL THESE VARIABLES HAPPEN AT THE CLASS LEVEL NOT THE OBJECT LEVEL GOSH DARN THAT'S CONFUSING
    #So, when there's a comSocket, it connects to all the other sockets? I don't know what's happening here.
    waiters = set()

    cache = []
    cache_size = 100

    #This function is called whenever someone joins
    def open(self):
        #ANYTIME SOMEONE JOINS, set the specific name of the object to the IP of the connector
        self.my_name = self.request.remote_ip
        #When something gets opened, we add that SPECIFIC OPENING to the waiters
        ComSocket.waiters.add(self)
        print(self.request.remote_ip + " has connected")
        global GAME_WORLD
        self.game_world = GAME_WORLD
        #When it opens, add a user to the world that is my name
        self.game_world.add_user(self.my_name)

    def on_close(self):
        #Anytime someone leaves, remove the user from the world
        self.game_world.remove_user(self.my_name)
        #Then, we remove the OBJECT ComSocket from the CLASS'S waiters set
        ComSocket.waiters.remove(self)
        
    def on_message(self, message):
        #ANYTIME WE GET A HIT FROM SOMETHING
        #We received it as a JSON, so we decode that
        parsed = tornado.escape.json_decode(message)
        #We make a dictionary 
        chat = {
            "id": str(uuid.uuid4()),
            #The body is the parsed body of the received message
            "body": parsed["body"]
            }
        #Now we add another thing to it because I don't know.
        #We render a string
        chat["html"] = tornado.escape.to_basestring(
            self.render_string("message.html", message=chat))

        #Sends 1 message to the world, receives a list of messages from the world. The list can be empty.
        #I pass in the 
        return_list_of_messages = self.send_message_to_world(chat["body"])

        #Find users and pass returned messages to them
        #COMMENTING OUT WHILE TESTING ABSURDITY
        #self.pass_messages_to_users(return_list_of_messages)
        #AND IT RESOLVES WHYYYYYY
        waiters_listified = list(self.waiters)
        #for every message we received
        for m in return_list_of_messages:
            #then, check every waiter
            for w in waiters_listified:
                #if this is a message this waiter should receive
                if m.to_user_id == w.my_name:
                    #built the chat
                    chat = {
                        "id": str(uuid.uuid4()),
                        "body": m.string_message
                        }
                    print(m.string_message)
                    #send the chat
                    print(chat)
                    chat["html"] = tornado.escape.to_basestring(
                        self.render_string("message.html", message=chat))
                    #send_updater writes something to a particular user
                    self.send_updater(chat, w)
                    
    @classmethod                
    def pass_messages_to_users(self, new_list_of_messages):
        #I turn the waiters into a list because I don't know how to handle a set. I should look this up sometime
        waiters_listified = list(self.waiters)
        #for every message we received
        for m in new_list_of_messages:
            #then, check every waiter
            for w in waiters_listified:
                #if this is a message this waiter should receive
                if m.to_user_id == w.my_name:
                    #built the chat
                    chat = {
                        "id": str(uuid.uuid4()),
                        "body": m.string_message
                        }
                    print(m.string_message)
                    #send the chat
                    print(chat)
                    chat["html"] = tornado.escape.to_basestring(
                        self.render_string("index.html", message=chat))
                    #send_updater writes something to a particular user
                    self.send_updater(chat, selected_waiter)

    #this actually writes the thing in a waiters box
    def send_updater(self, selected_message, selected_waiter):
        try:
            #ONLY SEND TO THAT WAITER
            selected_waiter.write_message(selected_message)
        except:
            print("DID NOT SEND")

    
    def send_message_to_world(self, created_chat):
        sending_message = message.Message(self.my_name, "world", created_chat)
        #A list of messages is returned here.
        return self.game_world.receive_message(sending_message)
    
            
class LoginToThis():
    @gen.coroutine
    def get(self):
        self.write("You hit the login page, yay!")


#This funtion begins the server
def beginServer(new_game_world):
    #Dunno what this does
    tornado.options.parse_command_line()
    app = Application()
    app.listen(8888)
    global GAME_WORLD
    GAME_WORLD = new_game_world
    tornado.ioloop.IOLoop.instance().start()
