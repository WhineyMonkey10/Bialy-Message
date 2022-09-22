#Only use for testing, this will drop the database
from replit import db
def dropbase(drop):
  del db[drop]