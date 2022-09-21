
## Imports

from replit import db
import colorama
import flask
import random
import time

# Get username, and userid
userid = db["client_user"]
del db["client_user"]
print(f"{colorama.fore.GREEN} User ID: {userid}")
