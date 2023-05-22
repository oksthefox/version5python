#!/usr/bin/python3
username = input("enter your name: ")
age = input ("enter your age: ")
copy = input("enter number of copies that you want: ")
print(username + " will be 100 years old in " + str(100-int(age)) + " years")


for x in range(0,int(copy)) :
    print(username + " will be 100 years old in " + str(100-int(age)) + " years" + "\n" )
