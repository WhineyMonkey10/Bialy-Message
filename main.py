#from src.server.user_connect import *
from server.handlers.connect import usersetup
from server.handlers.message_send import *
from server.handlers.message_receive import *
#from replit import db
import colorama
import flask
from flask import Flask, render_template, request, redirect, url_for
#from dropbase import *
from os import getcwd

##



#connectionid = usersetup()

#if chatuser == "":

#elif chatuser != "":


main = Flask(__name__)
main.template_folder = getcwd() + '/client/pages'
main.static_folder = getcwd() + '/client/static'


@main.route("/")
def index():
    return render_template("index.html")
main.run()

# testmessage()
# while True:
    # receive_message()
    # message = input(
        # f"{colorama.Fore.MAGENTA}Message to send: \n {colorama.Fore.RESET}")
    #print(f"{colorama.Fore.GREEN}Mesage Sent")
    # message_send(message)
