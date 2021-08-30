import enum
from pymongo import MongoClient
import json
# 방법1 - URI
# mongodb_URI = "mongodb://localhost:27017/"
# client = MongoClient(mongodb_URI)

# 방법2 - IP, PORT
client = MongoClient('localhost', 27017)

print(client.list_database_names())
local = client.local
a= local.firstCollection.find()
for i in a:
    print("i: type",type(i))
    print(dir(i))
    print(i.keys())
    q = i['person']['publication']
    for num, a in enumerate(q):
        if a['label'] == '1':
            print(num,"번째 q의 label = 1")
        elif a['label'] == '2':
            print(num,"번째 q의 label = 2")
        elif a['label'] == '3':
            print(num,"번째 q의 label = 3")
        elif a['label'] == '4':
            print(num,"번째 q의 label = 4")
        elif a['label'] == '0':
            print(num,"번째 q의 label = 0")
        elif a['label'] == '5':
            print(num,"번째 q의 label = 5")
        elif a['label'] == '6':
            print(num,"번째 q의 label = 6") 
        elif a['label'] == '7':
            print(num,"번째 q의 label = 7") 
        elif a['label'] == '8':
            print(num,"번째 q의 label = 8")    







    # data = json.dumps(i,indent=4)
    # print(data)