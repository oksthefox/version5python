#!/usr/bin/python3

#program that returns a list that contains only the elements that are common between the lists 

import random

a = [ 1 , 2 , 33 , 4 , 55 , 6 , 72 , 84 , 9 , 10 , 1 , 33, 55 , 80 , 4]



b = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 , 11 , 12]


ab = a + b

newAB =[]

print ("this is the set : ")
print (set(ab))

for x in set(ab):
  if a.count(x) >= 1 and b.count(x) >= 1:
    newAB.append(x)

print ( "this is the list that contains elements that are common between the lists : " )
print(newAB)

#Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates

def funlist(newlist:list):
  return list(set(newlist))
  
print (funlist(a))
  

def randomlist():
 
  newlist = []
  for x in range(1,30):
    number=random.randint(1,30)
    newlist.append(number)
  print ("successfully created a list: ")
  print (newlist)
  return newlist




newrandomlist=randomlist()