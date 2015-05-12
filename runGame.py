#This class does all the calls to all the appropriate files and runs the game server
import networkServer
import gameWorldInterface
import message

#We create threads for each of the clients. Those threads run outside
#of what we care about.

#The server's run function is what we want to hit. 
someInterface = gameWorldInterface.gameWorldInterface()

myNetwork = networkServer.Server(someInterface)
myNetwork.run()
