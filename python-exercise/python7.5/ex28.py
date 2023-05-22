#! /usr/bin/python3

num1 = input("choose a number: ")
num2 = input("choose a number: ")
num3 = input("choose a number: ")
#number_list = [x, y, z]

def thelargest (x:int , y:int, z:int):
 #   listnumber = [infinite values]
 #   list.sort()
 #   print(list[-1])
    if (x > y and x > z):
        print(x, "is bigger")
    elif (y>x and y>z):
        print(y, "is bigger")
    elif (z>x and z>y):
        print(z, "is bigger")
    else:
        print("all num equal")



thelargest(num1, num2, num3)