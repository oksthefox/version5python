#!/usr/bin/python3
import random

a=[1, 1, 4, 5, 31, 50, 40 ,33, 10 ,11 ]
b=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
for x in a:
    if x in b:
        print (x)

ranA = int(input("enter number for a range for list number 1: "))
ranB = int(input("enter number of range for list number 2: "))
c = [random.randint(1,101) for _ in range(ranA)]
d = [random.randint(1,101) for _ in range(ranB)]
for x in c:
    if x in d:
        print("This numbers are in both lists: ")
        print(x)
