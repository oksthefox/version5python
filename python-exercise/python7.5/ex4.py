#!/usr/bin/python3
num = int(input("ENTER ANY NUMBER: "))
x = range(1,num+1)
list = []
list = [i for i in x if num%i==0]
print(list)


#newlist=[]

#for i in x:
#    if num%i==0:
#        newlist.append(i)

#print (newlist)
