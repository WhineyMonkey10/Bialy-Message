from temparchive.src.database import mathbig
import colorama
from replit import db
import random

chatuser = input("Enter a username to chat (no spaces): ")
chatusermsg = input("User to chat to (Eg. user#0000): ")


def usersetup(output):
    notid = output
    connectionid = (f"{chatuser}#{random.randint(1, 9999)}")
    if output == id:
        return connectionid

def chattouser():
    chattouser = chatusermsg
    return chattouser


#def connectionid():

#db["users_connected"] = {"users": connectionid, "users": db.get("users_connected")}

#print(db.get("users_connected"))

#db[""] = "value"
