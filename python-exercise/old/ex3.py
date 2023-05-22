#!/usr/bin/python3

a = [ 1 , 2 , 33 , 4 , 55 , 6 , 72 , 84 , 9 , 10 ]

for x in a:
  if x<5:
    print(x)


newA = [ x for x in a if x < 5 ]
print( newA )


# user put a number and then it return a list that contains only elements from a list that are smaller then the number it was givven



while True:

  num = input( "Enter a number: ")  
  if not num.isdigit():
    print("You need to enter a number")
    continue
  else:
    break

numA = [ x for x in a if x < int(num) ]
print(numA)    

