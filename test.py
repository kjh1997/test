import enum
from pymongo import MongoClient
import json
import os
import time
temp = 0
name = []
nextdir = "C:/Users/kjh19/OneDrive/바탕 화면/test/json_data"
def search(dirname):
    filenames = os.listdir(dirname)
    for filename in filenames:
        full_filename = os.path.join(dirname, filename)
      
        if full_filename[-4:] == "json":
            name.append(full_filename)

search("C:/Users/kjh19/OneDrive/바탕 화면/test/")


for i in name:
    
    with open(i) as json_file:
        json_data = json.load(json_file)
    with open(i) as json_file:
        json_data2 = json.load(json_file)    
    pubdata = json_data['person']['publication']
    
    json_data2['person']['publication'].clear()
    
    # print("json_data", json_data)
    # print("basedata", basedata)
    labellist = []
    for i in pubdata:
        labellist.append(i['label'])
    setlabellist = list(set(labellist))
    print(sorted(setlabellist))
    for poplabellist in setlabellist:
        cnt=0
        basedata = json_data2
        for num, i in enumerate(pubdata):
            if poplabellist == i['label']:
                cnt +=1
                print("확인" , poplabellist, i['label'])
                print(i)
                basedata['person']['publication'].append(i)
        print(basedata)
        print(cnt , " : 개")
        print("label 하나 종료", poplabellist)

        #------------------- 초기화 ------------------------ 
        
        json_data2['person']['publication'].clear()
        cnt=0
        print("---------------------------------------다음------------------------------------------------")
        time.sleep(2)
        
    





    
    # print(i, " " ,labellist)
    # auname = i.split("/")[-1:][0]
    # for num, label in enumerate(labellist):    
    #     for i in a:
            
        
    #         if i['label'] == label:
    #             inputdata= {}
        
    
# C:/Users/kjh19/OneDrive/바탕 화면/test/json_data






















# client = MongoClient('localhost', 27017)

# print(client.list_database_names())
# test = client['test']
# a= test.test_data.find()


# for i in a:
#     print(i['person']['FullName'])
#     profile = i['person']['FullName']
#     # print("i: type",type(i))
    
#     # print(i.keys())
#     q = i['person']['publication']
    
#     for num , c in enumerate(q):
#         for b in range(10):

#             name = profile+"#"+str(i) 
#             print(name)
#             if c['label'] == b:
#                 name = q['person']['publication'].insert(a[num])
            
#         print(name)
        
        








    # for num, a in enumerate(q):
    #     if a['label'] == '1':
    #         print(num,"번째 q의 label = 1")
    #     elif a['label'] == '2':
    #         print(num,"번째 q의 label = 2")
    #     elif a['label'] == '3':
    #         print(num,"번째 q의 label = 3")
    #     elif a['label'] == '4':
    #         print(num,"번째 q의 label = 4")
    #     elif a['label'] == '0':
    #         print(num,"번째 q의 label = 0")
    #     elif a['label'] == '5':
    #         print(num,"번째 q의 label = 5")
    #     elif a['label'] == '6':
    #         print(num,"번째 q의 label = 6") 
    #     elif a['label'] == '7':
    #         print(num,"번째 q의 label = 7") 
    #     elif a['label'] == '8':
    #         print(num,"번째 q의 label = 8")    







    # data = json.dumps(i,indent=4)
    # print(data)