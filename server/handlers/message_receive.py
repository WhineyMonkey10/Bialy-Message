#from replit import db
import pymongo
import time

#client
client = pymongo.MongoClient(
    ""
)
db = client.db_name


#print(db.list_collection_names())
#db.create_collection("messages")
#def receive():
#    my_collection = db.messages
#    for received_message in my_collection.find({"delivered": False}):
#    #  received_message = my_collection.find()  #query for not delivered flag
#      print(received_message['message'])
#      time.sleep(0.5)
#      my_collection.update_one({"_id": received_message['_id']}, {"$set": {"delivered": True}})
#
def receive_message():
    my_collection = db.messages
    for received_message in my_collection.find({"delivered": False}):
        print(received_message['message'])
        time.sleep(0.5)
        my_collection.update_one({"_id": received_message['_id']}, {"$set": {"delivered": True}})
    return received_message
    