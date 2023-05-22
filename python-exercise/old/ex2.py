#!/usr/bin/python3
st = str(input("enter an input: "))
print (st[::-1])


if st == st[::-1]:
  print ("palindrom")
else:
  print ("not palindrom")    
