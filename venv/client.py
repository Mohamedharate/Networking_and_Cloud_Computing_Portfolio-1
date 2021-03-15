import socket, sys, random

IP = sys.argv[1]
PORT = int(sys.argv[2])
BOT = sys.argv[3]

RECV_BUFFER = 4096

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print('Waiting for connection response')

try:
    client_socket.connect((IP, PORT))
    client_socket.send(str.encode(BOT))

except socket.error as e:
    print(str(e))

bots = ["alice", "bob", "dora", "chuck"]

found = False

def findbot(bot):
    for b in bots:
        if bot == b:
            found = True
            break

    if found:
        return True
    else:
        return False
        #f"No bot with name {bot} found"


def alice(a, b = None):
 return "I think {} sounds great!".format(a + "ing")

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

    if findbot(BOT):
        send = eval(BOT + "(res.decode())")

    client_socket.send(send.encode())
