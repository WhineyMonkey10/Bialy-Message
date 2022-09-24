#Only works with ReplIT  version. https://github.com/WhineyMonkey10/Bialy-Message/tree/repl-database
#Only use for testing, this will drop the database
from replit import db
def dropbase(drop):
  del db[drop]