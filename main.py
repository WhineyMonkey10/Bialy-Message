#from src.server.user_connect import *
from server.connect import *
#from dropbase import *

##
currentuserid = connect()
keys = db.keys()
db["client_user"] = [currentuserid]
print(currentuserid)
