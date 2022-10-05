class Product :
    def __init__(self,id,name,price):
        self.id    = id
        self.name  = name
        self.price = price

    def __str__(self) :

        return f'Product ( id : {self.id} , name : {self.name}, price : {self.price}'   

from datetime import datetime
from random import randint
DT = datetime.now()
day =DT.strftime("%y-%m-%d-%H-%M-%S")
n = randint(1,999999)


def new_id ():
   id = (f'{day}-{n}')
   return id        

p1= Product ( new_id(),'Samsung Galaxy', 100000)
print(p1)



x=[]
for i in range (100):
    x.append(new_id())
print(x)
