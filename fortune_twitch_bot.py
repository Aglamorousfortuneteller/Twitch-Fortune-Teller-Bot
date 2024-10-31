import socket
import random
import time

HOST = 'irc.chat.twitch.tv'
PORT = 6667

TOKEN="YOUR_OAUTH_TOKEN"        # OAuth token for your Twitch bot
CHANNEL="YOUR_CHANNEL_NAME"     # Twitch channel name where the bot connects
NICKNAME="YOUR_BOT_NICKNAME"    # The bot's username

# Load fortunes and predictions from text files
def load_lines(filename):
    with open(filename, "r") as file:
        return [line.strip() for line in file if line.strip()]

fortunes = load_lines("fortunes.txt")
predictions = load_lines("predictions.txt")

def openSocket():
    s = socket.socket()
    s.connect((HOST, PORT))
    s.send((f"PASS " + TOKEN + "\r\n").encode('utf-8'))
    s.send((f"NICK " + NICKNAME + "\r\n").encode('utf-8'))
    s.send((f"JOIN #" + CHANNEL + "\r\n").encode('utf-8'))
    return s

def sendMessage(s, message):
    messageTemp = f"PRIVMSG #" + NICKNAME + " :" + message
    s.send((messageTemp + "\r\n").encode('utf-8'))
    print("Sent: " + messageTemp)

def joinRoom(sock):
    readBuffer = ""
    Loading = True
    while Loading:
        readBuffer = readBuffer + sock.recv(2048).decode('utf-8')
        temp = readBuffer.split('\n')
        readBuffer = temp.pop()
        for line in temp:
            print(line)
            Loading = loadingComplete(line)
    sendMessage(sock, 'Ask: Tell me my future! Or type "🔮" with your yes or no question')

def loadingComplete(line):
    return "End of /NAMES list" not in line

def getUser(line):
    separate = line.split(":", 2)
    user = separate[1].split("!", 1)[0]
    return user

def getMessage(line):
    return line

s = openSocket()
joinRoom(s)
readbuffer = ""

while True:
    readbuffer = readbuffer + s.recv(2048).decode('utf-8')
    temp = str.split(readbuffer, "\n")
    readbuffer = temp.pop()
    for line in temp:
        user = getUser(line)
        message = getMessage(line)

        if "ping" in message.lower():
            sendMessage(s, "@" + user + ", PONG")
            break
        if "Kissahomie" in message:
            sendMessage(s, "@" + user + " Kissahomie")
            break
        if "HeyGuys" in message:
            sendMessage(s, "@" + user + " Hi!")
            break
        if "<3" in message:
            sendMessage(s, "@" + user + " 💖💖💖")
            break
        if "hi" in message.lower():
            sendMessage(s, "@" + user + " HeyGuys")
            break
        if "crystal ball" in message.lower() or "🔮" in message:
            sendMessage(s, "🔮 Crystal ball says... " + random.choice(fortunes))
            break
        if "Thanks for following," in message:
            sendMessage(s, "thanks for follow! 💖💖💖")
            break
        if "Hey! I want my future to be told" in message or "Tell me my future!" in message or "future" in message.lower():
            sendMessage(s, "Calling Satan since God doesn't pick up...")
            sendMessage(s, "...")
            sendMessage(s, "✨✨✨")
            sendMessage(s, random.choice(predictions))
            break
