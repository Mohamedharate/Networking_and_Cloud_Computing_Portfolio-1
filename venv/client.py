import socket, sys, random

bots = ["quotes", "bob", "dora", "chuck"]

if sys.argv[1] == "--help" or sys.argv[1] == "-h":
    print(f"You have to write in the following format:\npython client.py YOUR-IP-ADDRESS YOUR-PORT BOT_NAME"
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

def quotes(a, b = None):

    wordsInArray = a.split()

    ACTIONS = {
        ("hey","hello","hi"):["Hey there!","Hey!","Hey beauty!"],
        ("sup","zup","what's up","what is up","how are you","how r u"):["Just chilling!","I am talking to you!","Just about to sleep"],
        ('eat','hungry','meal','bite','snack',"dinner"): ["All you do is eating!","You have eaten too much already!","Bon aptit!"],
        ('help',''): ["Ask Google!","Sorry, I can't help you!","I am here to help you!"],
        ('code','coding','programming'): ["fuck coding","shut up","I love coding"],
        ('joke','wqeqweq'): ["fd"],
        ('sleep','ewe'): ["ddf"],
        ('sing','ewe'): ["ddf"],
        ('dwin','qweqe'): ["fffff"]
    }

    found = False
    for keysList in ACTIONS:
        for key in keysList:
            for word in wordsInArray:
                if key.__eq__(word.lower()):
                    found = True
                    ress1 = ACTIONS[keysList]
                    ress = (random.choice(ress1))
                    break

    if not found:
        ress1 = random.choice(list(ACTIONS.values()))
        ress = (random.choice(ress1))

    return str(ress)

def bob(a, b = None):
 if b is None:
    return "Not sure about {}. Don't I get a choice?".format(a + "ing")
 return "Sure, both {} and {} seems ok to me".format(a, b + "ing")

def dora(a):
 alternatives = ["coding", "singing", "sleeping", "fighting"]
 b = random.choice(alternatives)
 res = "Yea, {} is an option. Or we could do some {}.".format(a, b)
 return res

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
    res = client_socket.recv(RECV_BUFFER)

    if res.decode().lower() == disconnect:
        client_socket.close()

    if res:
        print("Host: " + res.decode('utf-8'))

    sendMSG = eval(BOT + "(res.decode())")

    client_socket.send(sendMSG.encode())