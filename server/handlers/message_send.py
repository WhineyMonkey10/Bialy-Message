## Imports

#from replit import db
import colorama
import flask
import random
import time
from .connect import *
import pymongo
import os

#client
client = pymongo.MongoClient(
    "string"
)

#print(db.list_collection_names())
#db.create_collection("messages")
db = client.db_name
# Send message


def message_send(message):
    #message = f"{colorama.Fore.BLUE}{usersetup()}: {colorama.Fore.MAGENTA}{message}"
    message = f"{usersetup(id)}: {message}"
    insert_message = {
        "message": message,
        "touser": chattouser(),
        "delivered": False
    }
    my_collection = db.messages
    my_collection.insert_one(insert_message)
    failed = False
    if db != client.db_name:
        failed = True
    return failed


# Get username, and userid


def testmessage():
    print(
        f"{colorama.Fore.GREEN}User ID: {usersetup(id)}. Sending chat message to test connection..."
    )
    message = "Hello World"

    error = False
    if message_send(message) == False:
        print(f"{colorama.Fore.BLUE} Test sucsessful. {colorama.Fore.WHITE}")
    else:
        print(
            f"{colorama.Fore.RED} Test failed, please report the error on GitHub"
        )
