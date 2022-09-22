from temparchive.src.database import mathbig
import colorama
from replit import db
import random

def usersetup():
    chatuser = input("Enter a username to chat: ")
    connectionid = (f"{chatuser}{random.randint(1, 9999)}")
    return connectionid

#def connectionid():

  #db["users_connected"] = {"users": connectionid, "users": db.get("users_connected")}
  
  #print(db.get("users_connected"))

  
    

    #db[""] = "value"
