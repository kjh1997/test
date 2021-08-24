from _typeshed import NoneType


a = [ 1, 2 , 3,5,6, None , 7]
print(type(a[5]))
print(type(None))

for num in range(len(a)):
    if type(a[num]) == None:
        continue
    print(num) 