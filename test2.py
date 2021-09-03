import json
car_group = dict()
k5 = dict()

k5["price"] = "5000"

k5["year"] = "2015"

car_group["K5"] = k5
avante = dict()

avante["price"] = "3000"

avante["year"] = "2014"

car_group["Avante"] = avante
#json 파일로 저장

with open('C:/Users/kjh19/OneDrive/바탕 화면/test', 'w', encoding='utf-8') as make_file:
    json.dump(car_group, make_file, indent="\t")

