#!/usr/bin/python3
num_of_Fibonnaci = int(input("Enter how many numbers: "))



def createFib(number):
    fibonacci = []
    if number==0:
        print(fibonacci)
    elif number==1:
        fibonacci = [1]
    elif number == 2:
        fibonacci = [1, 1]
    else:
        fibonacci = [1,1]
        for x in range(2,number):
            fibonacci.append(fibonacci[x-2]+fibonacci[x-1])
    return fibonacci

print (createFib(num_of_Fibonnaci))