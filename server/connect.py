from temparchive.src.database import mathbig

from replit import db
import random

def connect():
  chatuser = input("Enter a username to chat: ")
  connectionid = (f"{chatuser}{random.randint(1, 9999)}")
  print(f"Connected to server with username {connectionid}. Sending chat message to test connection.")
  #db["users_connected"] = {"users": connectionid, "users": db.get("users_connected")}
  
  #print(db.get("users_connected"))
  return (connectionid)
    

    #db[""] = "value"
