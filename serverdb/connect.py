from temparchive.src.database import mathbig

from replit import db
import random
chatuser = input("Enter a username to chat: ")
connectionid = (f"{chatuser}{random.randint(1, 9999)}")
def connect():

  
  db["users_connected"] = {"newuser": connectionid, "users": db.get("users_connected")}
  
  print(db.get("users_connected"))
  return (f"User connected with ID: {connectionid}")
    

    #db[""] = "value"
