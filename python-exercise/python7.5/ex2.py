#!/usr/bin/python

num = int(input(" enter a number: "))

if num%4==0:
    print("This number is divides by 4")
elif num%2==0:
    print("The number that you chose is even ")
else:
    print("The number that you chose is odd")

num = int(input("enter a number: "))
check = int(input("enter another number: "))

if check%num==0:
    print(str(check) + " divides evenly into " + str(num))
else:
    print(str(check) + " not divides evenly into " + str(num))