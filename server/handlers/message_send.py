
## Imports

from replit import db
import colorama
import flask
import random
import time
from .connect import *


# Send message

def message_send(message):
  db["newmessage"] = message

# Get username, and userid

def testmessage():
  print(f"{colorama.Fore.GREEN}User ID: {usersetup()}. Sending chat message to test connection")