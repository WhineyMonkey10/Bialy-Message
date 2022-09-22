
#from src.server.user_connect import *
from server.handlers.connect import usersetup
from server.handlers.message_send import *
from server.handlers.message_receive import *
from replit import db
db["newmessage"] = "bob"
#from dropbase import *

##

#connectionid = usersetup()


#if chatuser == "":
      
#elif chatuser != "":
testmessage()
start_receiving()
while True:
  message = input("Message to send")
  message_send(message)
  
