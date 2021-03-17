import socket
import sys
import random
import re
import datetime
from datetime import date



bots = ["alice", "bob", "dora", "chuck"]

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



def getDate():
    d = datetime.date.today().strftime("%A, %B %d, %Y")
    return d

def getTime():
    t = datetime.datetime.now().strftime("%H:%M:%S")
    return t

def alice(a, b = None):
    wordsInArray = a.split()

    ACTIONS = {
        ('hey','hello','hi'):["Hey there!","Hey!","Hey beauty!"],
        ('sup','zup','how r u'):["Just chilling!","I am talking to you!","Just about to sleep"],
        ('eat','hungry','meal','bite','snack',"dinner"): ["All you do is eating!","You have eaten too much already!","Bon aptit!"],
        ('help','helping'): ["Ask Google!","Sorry, I can't help you!","I am here to help you!"],
        ('code','coding','programming'): ["fuck coding","shut up","I love coding","I hate coding"],
        ('joke','joking'): ["I don't like joking","If you want to be a computer science major, all you have do is get sick.\nBefore long you’ll be coughing and hacking.",
                            "Why didn't the client tip the server?\nBecause they didn't have enough cache!",
                            "How physicists see other sciences:\nBiology: squishy physics\nGeology: slow physics\nComputer Science: virtual physics\nPsychology: people physics\nChemistry: impure physics\nMath: physics minus the units"],
        ('sleep','sleepy','dream','dreaming','dreamt'): ["I am great in bed\nI can sleep for days","I dreamt I wrote The Hobbit the other night. I think I was\nTolkin in my sleep",
                             "Last night you were in my dream"],
        ('sing','shower','singing'): ["Never sing in the shower\nSinging leads to dancing,\nDancing leads to slipping\nand slipping leads to paramedics seeing\n YOU NEKED,\nSo REMEMBER Don't SING",
                            "I don't sing in the shower.\n\nI perform.","Singing in the shower is great until you\nget shampoo in mouth. Then it's more of a soap opera.",
                            ""],
        ('bye','byee'): ["oh noo","Byee :/"]
    }

    if len(wordsInArray) >= 1:
        found = False
        for keysList in ACTIONS:

            for key in keysList:

                for word in wordsInArray:

                    if word == key:
                        found = True
                        ress1 = ACTIONS[keysList]
                        ress = (random.choice(ress1))

    if not found and len(wordsInArray) == 1:
        ress = "Not sure about {}. Don't I get a choice?".format(wordsInArray[0] + "ing")

    elif not found:
        ress1 = random.choice(list(ACTIONS.values()))
        ress = (random.choice(ress1))

    return str(ress)


def bob(a, b = None):

    wordsInArray = a.split()

    ACTIONS = {
        ('hey', 'hello', 'hi'): ["Hey there!", "Hey!", "Hey beauty!"],
        ('sup', 'zup'): ["Just chilling!", "I am talking to you!", "Just about to sleep"],
        ('eat', 'hungry', 'meal', 'bite', 'snack', "dinner"): ["All you do is eating!",
                                                               "You have eaten too much already!", "Bon aptit!","I don't eat!"],
        ('help', 'helping'): ["Ask Google!", "Sorry, I can't help you!", "I am here to help you!"],
        ('code', 'coding', 'programming'): ["f* coding", "shut up", "I love coding", "I hate coding"],
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
        ('day', 'date'): [f"Today is: {getDate()}"],
        ('time', 'oclock'): [f"Time is: {getTime()}"],
        ('bye', 'byee'): ["oh noo", "Byee :/"],
        ('who', 'whoami'): [f"I am {BOT.upper()}!"]
    }

    if len(wordsInArray) >= 1:
        found = False
        for keysList in ACTIONS:

            for key in keysList:

                for word in wordsInArray:

                    if word == key:
                        found = True
                        ress1 = ACTIONS[keysList]
                        ress = (random.choice(ress1))

    if not found and len(wordsInArray) == 1:
        ress = "Not sure about {}. Don't I get a choice?".format(wordsInArray[0] + "ing")

    elif not found:
        ress1 = random.choice(list(ACTIONS.values()))
        ress = (random.choice(ress1))


    return str(ress)


def dora(a):

    wordsInArray = a.split()
    a = random.choice(wordsInArray)

    alternatives = ["coding", "singing", "sleeping", "fighting"]
    b = random.choice(alternatives)
    res = "Yea, {} is an option. Or we could do some {}.".format(a, b)
    return str(res)

def chuck(a, b = None):
    wordsInArray = a.split()
    a = random.choice(wordsInArray)
    action = a + "ing"
    bad_things = ["fighting", "bickering", "yelling", "complaining"]
    good_things = ["singing", "hugging", "playing", "working"]
    if action in bad_things:
        return "YESS! Time for {}".format(action)
    elif action in good_things:
        return "What? {} sucks. Not doing that.".format(action)
    return "I don't care!"


while True:

    disconnect = f"bye {BOT}"
    MSG_FROM_SERVER = client_socket.recv(RECV_BUFFER).decode('utf-8').lower()


    if MSG_FROM_SERVER == "host":
        MSG_FROM_SERVER = client_socket.recv(RECV_BUFFER).decode('utf-8').lower()
        MSG_FROM_SERVER = MSG_FROM_SERVER.replace('host','')
        if disconnect in MSG_FROM_SERVER:
            client_socket.close()

        if MSG_FROM_SERVER:
            print("Host: " + MSG_FROM_SERVER.upper())

        MSG_FROM_SERVER = re.sub("[^A-Za-z]+"," ",MSG_FROM_SERVER).lower()


        sendMSG = eval(BOT + "(MSG_FROM_SERVER)")

        client_socket.send(sendMSG.encode())
        print("ME: " + sendMSG)
    else:
        print((MSG_FROM_SERVER).upper())

