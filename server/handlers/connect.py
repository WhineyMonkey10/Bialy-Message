from temparchive.src.database import mathbig
import colorama
import random
import pymongo

chatuser = input("Enter a username to chat (no spaces): ")

client = pymongo.MongoClient(
    "s"
)
db = client.db_name

def usersetup(output):
    my_collection = db.online_users
    notid = output
    connectionnumber = random.randint(1, 9999)
    connectionid = (f"{chatuser}#{connectionnumber}")

    if output == id:
        return connectionid

    else:

        my_collection = db.online_users
        if my_collection.find_one({connectionnumber}) == None:
            insert_user = {
                "username": chatuser,
                "connectionid": connectionid
            }
            my_collection.insert_one(insert_user)
            print(f"{colorama.Fore.GREEN}User ID: {connectionid}")

        else:
            print(f"{colorama.Fore.RED}User ID: {connectionid} already exists")



#def connectionid():

#db["users_connected"] = {"users": connectionid, "users": db.get("users_connected")}

#print(db.get("users_connected"))

#db[""] = "value"
