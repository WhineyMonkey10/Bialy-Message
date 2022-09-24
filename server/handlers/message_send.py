
## Imports

from replit import db
import colorama
import flask
import random
import time
from .connect import *
import pymongo
import os

#client
connection_string = load_dotenv()
client = pymongo.MongoClient("string")
load_dotenv()
string = os.getenv()
#print(db.list_collection_names())
#db.create_collection("messages")

# Send message

def message_send(message):
  #message = f"{colorama.Fore.BLUE}{usersetup()}: {colorama.Fore.MAGENTA}{message}"
  message = f"{usersetup()}: {message}"
  insert_message = { "message": message}
  my_collection = db.messages
  my_collection.insert_one(insert_message)
# Get username, and userid

def testmessage():
  print(f"{colorama.Fore.GREEN}User ID: {usersetup()}. Sending chat message to test connection...")
  message = "Hello World"
  message_send(message)
