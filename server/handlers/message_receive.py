from replit import db
import colorama
import pymongo

#client
client = pymongo.MongoClient("string")
db = client.db_name
#print(db.list_collection_names())
#db.create_collection("messages")
def receive():
    my_collection = db.messages
    received_message = my_collection.find_one()
    print(received_message)
    #del db["newmessage"]
