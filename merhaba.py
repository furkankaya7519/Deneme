from pymongo import MongoClient
from bson import Code

client = MongoClient("mongodb+srv://softwareunopro:Unopro0101@cluster0.sys4qgi.mongodb.net/?retryWrites=true&w=majority")
db = client['upeyesData']
collection = db['measurements']

def Deneme1():
    
    my_code = Code('for i in range(10):\n    print("Furkan")', {})
    my_doc = {'version': 1, 'code': my_code}
    collection.insert_one(my_doc)

def RunCode():
    document = collection.find_one({"codeReference": "true"})
    if document:
        which_version = document['WhichVersion']
        print(which_version)
    else:
        print("Belge bulunamadı.")
    
    document = collection.find_one({"version":which_version})
    exec(document['code'])





#Deneme1()

RunCode()




