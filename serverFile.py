from socket import *
myHost = ''
myPort = 50007
sockobj = socket(AF_INET, SOCK_STREAM)
sockobj.bind((myHost, myPort))
sockobj.listen(5)

listofpersons = []

class personObject:
    Name = ""
    Description = ""
    Location = [0, 0]

    def __init__(self, nameString):
        self.Name = nameString
        self.Location = [0,0]
        self.Description = ""

def interpretIncoming(data):
    print('Got Data from client:' + data)
    myincoming = data.split(sep=',')
    if myincoming[0] == 'Create':
        newperson = personObject(myincoming[1])
        listofpersons.append(newperson)
        return str.encode("Created a new person with a name:" +
                          newperson.Name +
                          " at location:" + str(newperson.Location))
    if myincoming[0] == 'Move':
        myperson = getPersonFromName(myincoming[1])
        movePerson(myperson, myincoming[2])
        return str.encode(myperson.Name + " has moved to " +
                          str(myperson.Location))
    if myincoming[0] == 'Description':
        myperson = getPersonFromName(myincoming[1])
        describePerson(myperson, myincoming[2])
        return str.encode(myperson.Name + "'s description is now: " +
                          myperson.Description)
    else:
        return str.encode(data)

def getPersonFromName(personname):
    for x in listofpersons:
        if x.Name == personname:
            return x

def movePerson(myperson, direction):
    if direction == "west":
        myperson.Location = [myperson.Location[0] - 1, myperson.Location[1]]
    if direction == "east":
        myperson.Location = [myperson.Location[0] + 1, myperson.Location[1]]
    if direction == "north":
        myperson.Location = [myperson.Location[0], myperson.Location[1] + 1]
    if direction == "south":
        myperson.Location = [myperson.Location[0], myperson.Location[1] - 1]

def describePerson(myperson, description):
    myperson.Description = description

while True:
    connection, address = sockobj.accept()
    print('Server connected by', address)
    while True:
        data = connection.recv(1024)
        if not data: break
        mynewdata = interpretIncoming(bytes.decode(data))
        connection.send(b'Echo=>' + mynewdata)
    connection.close()


