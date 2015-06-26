import tornadoServerTest
import faked_game_world
import gameWorldInterface
import threading
from multiprocessing import Process

newGameWorldInterface = gameWorldInterface.gameWorldInterface()

listOfThreads = []

gw = faked_game_world.FakeWorld(newGameWorldInterface)

print("Started Game World")
#listOfThreads.append(gw)

ts = threading.Thread(tornadoServerTest.beginServer(newGameWorldInterface))

print("Started Server side")
#listOfThreads.append(ts)


def loop_a():
    while 1:
        print("a")

def loop_b():
    while 1:
        print("b")

if __name__ == '__main__':
    #Process(target=loop_a).start()
    #Process(target=loop_b).start()
    Process(target=gw.start()).start()
    Process(target=ts.start()).start()
#OKAY, ONLY ONE THREAD GETS TO ACTUALLY GO EVERYONE ELSE DIES. WE RUN SERVER
#AND THAT'S THE END OF IT. I WILL CALL A FUNCTION ON THE WORLD EVERY TIME
#IT NEEDS TO GET A MESSAGE DONE
