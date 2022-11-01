import pymongo 
import os

DB_NAME = os.environ.get("DB_NAME","New-CaptionBot")
DB_URL = os.environ.get("DB_URL","mongodb+srv://aswanthvk:aswanthvk@cluster0.ul7sp2m.mongodb.net/?retryWrites=true&w=majority")
mongo = pymongo.MongoClient(DB_URL)
db = mongo[DB_NAME]
dbcol = db["user"]

def insert(chat_id):
            user_id = int(chat_id)
            user_det = {"_id":user_id,"caption":None , "date":0}
            try:
            	dbcol.insert_one(user_det)
            except:
            	value = 'new'
            	return value
            	pass

def addcaption(chat_id, caption):
       dbcol.update_one({"_id": chat_id},{"$set":{"caption": caption}})
	
def delcaption(chat_id): 
        dbcol.update_one({"_id": chat_id},{"$set":{"caption":None}})
	
def find(chat_id):
	id =  {"_id":chat_id}
	x = dbcol.find(id)
	for i in x:
             caption = i["caption"]
             return caption

def getid():
    values = []
    for key  in dbcol.find():
         id = key["_id"]
         values.append((id)) 
    return values
    
def find_one(id):
	return dbcol.find_one({"_id":id})
