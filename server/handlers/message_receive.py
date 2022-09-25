#from replit import db
import pymongo
import time
from .connect import *

#client
client = pymongo.MongoClient(
    "string"
)
db = client.db_name


#print(db.list_collection_names())
#db.create_collection("messages")
def receive():
    my_collection = db.messages
    userid = usersetup(id)
    for received_message in my_collection.find({"touser": userid, "delivered": False}):
    #  received_message = my_collection.find()  #query for not delivered flag
      print(received_message['message'])
      time.sleep(0.5)
      #my_collection.delete_many({})
