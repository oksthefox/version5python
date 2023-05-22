#!/usr/bin/python3
a = [1 ,1 ,2 ,3 ,4 ,5 ,8 ,99 ,88 ,77 ,66 ,55 ,44 ,33 ,67]
for x in a:
    if x<5:
        print(x)
newA =[x for x in a if x<5]
print(newA)
num = input("enter a number: ")
for x in a:
    if x< int(num):
        print (x)