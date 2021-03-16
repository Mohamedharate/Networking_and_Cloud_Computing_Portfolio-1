import socket, sys, random
from datetime import date
import re
from datetime import datetime



bots = ["alice", "bob", "dora", "chuck","customerservice"]

if sys.argv[1] == "--help" or sys.argv[1] == "-h" or sys.argv[3] == ' ':
    print(f"You have to write in the following format:\npython client.py"
          f" YOUR-IP-ADDRESS YOUR-PORT BOT_NAME"
          f"\nThis is a list of our bots:\n{str(bots)}")
    exit()

IP = sys.argv[1]
PORT = int(sys.argv[2])
BOT = sys.argv[3]
RECV_BUFFER = 4096

if BOT not in bots:
    print(f"No bot with name {BOT} found\nThis is a list of our bots:\n{str(bots)}")
    exit()

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client_socket.connect((IP, PORT))
    client_socket.send(str.encode(BOT))

except socket.error as e:
    print(str(e))

print('Waiting for connection response')

def alice(wordsInArray, b = None):

    ACTIONS = {
        ('hey','hello','hi'):["Hey there!","Hey!","Hey beauty!"],
        ('sup','zup','how r u'):["Just chilling!","I am talking to you!","Just about to sleep"],
        ('eat','hungry','meal','bite','snack',"dinner"): ["All you do is eating!","You have eaten too much already!","Bon aptit!"],
        ('help','helping'): ["Ask Google!","Sorry, I can't help you!","I am here to help you!"],
        ('code','coding','programming'): ["fuck coding","shut up","I love coding","I hate coding"],
        ('joke','joking'): ["I don't like joking","sdf"],
        ('sleep','ewe'): ["ddf","dfs"],
        ('sing','ewe'): ["ddf","fdsf","fds"],
        ('bye','byee'): ["oh noo","Byee :/"],
        ('dwin','qweqe'): ["fffff","dsfs","sdfs","sdf"]
    }


    found = False
    for keysList in ACTIONS:

        for key in keysList:

            for word in wordsInArray:

                if word == key:
                    found = True
                    ress1 = ACTIONS[keysList]
                    ress = (random.choice(ress1))

    if not found:
        ress1 = random.choice(list(ACTIONS.values()))
        ress = (random.choice(ress1))

    return str(ress)


def bob(wordsInArray, b = None):

    ACTIONS = {
        ('hey', 'hello', 'hi'): ["Hey there!", "Hey!", "Hey beauty!"],
        ('sup', 'zup'): ["Just chilling!", "I am talking to you!", "Just about to sleep"],
        ('eat', 'hungry', 'meal', 'bite', 'snack', "dinner"): ["All you do is eating!",
                                                               "You have eaten too much already!", "Bon aptit!"],
        ('help', 'helping'): ["Ask Google!", "Sorry, I can't help you!", "I am here to help you!"],
        ('code', 'coding', 'programming'): ["fuck coding", "shut up", "I love coding", "I hate coding"],
        ('joke', 'joking','jokes'):
            ["I don't like joking",
            "What did the fish say when he swam into a wall?\nDam.",
            "while (mahself.stillAwake())\n{\n   sleep++;\n}","What do you call when computer sience majors make fun of each other?\nCyber boolean!"
            "Prgramming is like writing a book..\nExcept when you miss a single comma on page 126 the whole thing makes no sense",
            "My dog ate my computer science project\nyour dog ate your coding assignment?\nIt took him a couple bytes",
            "I don't like computer science jokes...\nNot one bit.",
            "One thing I know is that a computer science major didn't name the original pokemon.\nOtherwise, charmander would evolve into stringmander.",
            "Why are people who use the metric system so good at computer science?\nBecause they are pro-grammers.",
            "I'm teaching my white blood cells math and my red blood cells computer science\nOnce they become STEM cells I am hoping to regrow a finger.",
            "I would talk about computer science...\nBut it makes my mother board"],
        ('day', 'date'): [f"Today's date: {date.today()}","we"],
        ('time', 'ewe'): [f"Time is: {datetime.now()}", "we", "we"],
        ('who', 'whoami'): [f"I am {BOT}!", "dsfs", "sdfs", "sdf"]
    }

    found = False
    for keysList in ACTIONS:

        for key in keysList:

            for word in wordsInArray:

                if word == key:
                    found = True
                    ress1 = ACTIONS[keysList]
                    ress = (random.choice(ress1))

    if not found:
        ress1 = random.choice(list(ACTIONS.values()))
        ress = (random.choice(ress1))

    return str(ress)

    '''
 if b is None:
    return "Not sure about {}. Don't I get a choice?".format(a + "ing")
 return "Sure, both {} and {} seems ok to me".format(a, b + "ing")

def dora(a):
 alternatives = ["coding", "singing", "sleeping", "fighting"]
 b = random.choice(alternatives)
 res = "Yea, {} is an option. Or we could do some {}.".format(a, b)
 return str(res)
 '''

def chuck(a, b = None):
 action = a + "ing"
 bad_things = ["fighting", "bickering", "yelling", "complaining"]
 good_things = ["singing", "hugging", "playing", "working"]
 if action in bad_things:
    return "YESS! Time for {}".format(action)
 elif action in good_things:
    return "What? {} sucks. Not doing that.".format(action)
 return "I don't care!"

def customerservice(a, b=None):
    if b is None:
        uselessness = random.choice(["Sorry, I can't help you with {}.".format(a + "ing"),
                                     "I don't understand, is there a problem?",
                                     "I will contact my supervisor at once!"])
        return uselessness
    uselessness = random.choice(["Do you need help with {} or {}?".format(a + "ing", b + "ing")])
    return uselessness

while True:

    disconnect = f"bye {BOT}"
    MSG_FROM_SERVER = client_socket.recv(RECV_BUFFER).decode('utf-8').lower()

    if MSG_FROM_SERVER == "host":
        MSG_FROM_SERVER = client_socket.recv(RECV_BUFFER).decode('utf-8').lower()

        if MSG_FROM_SERVER == disconnect:
            client_socket.close()

        if MSG_FROM_SERVER:
            print(MSG_FROM_SERVER.upper())

        MSG_FROM_SERVER = re.sub("[^A-Za-z]+"," ",MSG_FROM_SERVER).lower()

        wordsInArray = MSG_FROM_SERVER.split()

        sendMSG = eval(BOT + "(wordsInArray)")

        client_socket.send(sendMSG.encode())
        print("ME: " + sendMSG)
    else:
        print((MSG_FROM_SERVER).upper())
