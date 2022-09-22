from replit import db
import colorama

def receive():
    received_message = db["newmessage"]
    print(received_message)
    del db["newmessage"]
