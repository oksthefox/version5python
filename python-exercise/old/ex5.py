#!/usr/bin/python3

#Given a .txt file that has a list of a bunch of names, count how many of each name there are in the file
import sys

def countname( filename ):
  namecount = {}
  try:
    with open (filename, "r") as file:
      names = file.read().split()
  except:
    print(f"Error: Could not read file {filename}")    
    return namecount
    
  for name in names:
    if name in namecount:
       namecount[name] += 1
    else:
       namecount[name] = 1
  return namecount



print (countname(sys.argv[1]))
