import enum
from typing import Collection
from pymongo import MongoClient
import json
import os
client = MongoClient('localhost', 27017)
name = []
db = client["test"]
Coll = db["test_data"]



def search(dirname):
    filenames = os.listdir(dirname)
    for filename in filenames:
        full_filename = os.path.join(dirname, filename)
      
        if full_filename[-4:] == "json":
            name.append(full_filename)

search("C:/Users/kjh19/OneDrive/바탕 화면/test/")
print(name)
for i in name:
    with open(i) as json_file:
        
        json_data = json.load(json_file)
        print(i)
        Coll.insert_one(json_data)
        
        



# print(client.list_database_names())
# local = client.local
# a= local.firstCollection.find()

# a['test']
