from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/test')
db = client.test
#my dummy database is myDatabase.
coll1 = db.coll1 #selecting the coll1 in myDatabase
for document in coll1.find():
    print (document)