from replit import db
import colorama

def start_receiving():
  while True:
    received_message = value = db["newmessage"]
    print(received_message)
    del db["newmessage"]
