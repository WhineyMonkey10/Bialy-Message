#from src.server.user_connect import *
from server.handlers.connect import usersetup
from server.handlers.message_send import *
from server.handlers.message_receive import *
#from replit import db
import colorama
#from dropbase import *

##

#connectionid = usersetup()

#if chatuser == "":

#elif chatuser != "":
testmessage()
while True:
    receive()
    message = input(
        f"{colorama.Fore.MAGENTA}Message to send: \n {colorama.Fore.RESET}")
    #print(f"{colorama.Fore.GREEN}Mesage Sent")
    message_send(message)
