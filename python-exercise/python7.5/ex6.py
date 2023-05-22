#!/usr/bin/python3
word = str(input("Enter astring: "))
reverse_word = word[::-1]
if word == reverse_word:
    print("The word " + word+ " is polindrome" )
else:
    print("The word " + word+ " isn't polindrome")
   