#This is an example of a script that runs the game server

#game_server is the file with the server code
import game_server
#the faked game world is an example game world that runs
import faked_game_world

#Creates a game world
gw = faked_game_world.GameWorld()

#the game world is passed to the server's "beginServer" function to
#begin the server with the game world
game_server.beginServer(gw)

#NOTE: YOU NEED TO INSTALL TORNADO SERVER TO USE THIS
#DO A "pip install tornado" TO GET IT

#Things you can do with the server:
    #In your browser, go to "localhost:8888" to activate a connection
    #to the server.
        #User Ids are currently recorded by IP, so logging in as two internet
        #browsers on one computer doesn't work too well.
        #Try logging in with your phone. Using the command line, type "ipconfig" to
        #look up your local IP address, and point your phone to that. Your
        #phone will connect to the server hosted on your computer across
        #your wifi network.
    #You might want the server to end so you can type things in the command
    #line and look up values for the variables (such as the game world).
        #TO do this, have one of the connections point to "localhost:8888/ENDTHIS"
        #That sends the kill command to the server so that you get your
        #console back.
    #While connected, you can type a message and post it and it will send
    #through the server, get passed through the game world, and come back
    #out to the HTML
