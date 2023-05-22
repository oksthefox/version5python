#!/usr/bin/python3
import sys
import json
import os

def find_char(str):
    dic ={}
    try:
        for x in str:
            if x in dic:
                dic[x] += 1
            else:
                dic[x]= 1
        return dic
    except:
       print("BAD USAGE. EXPECTING 1 ARGUMENT")

def to_file(object:json):
    if len(sys.argv)==2:
        filename = str(sys.argv[2])

        if os.path.exists(filename) and filename.endswith(".json"):
            print("the file "+filename+" exists")
            with open(filename, "w") as file:
                file.write(json.dumps(object))
        else:
            print("the file "+ filename+" does not exists or doesnt end with .json")
    else:
        print("invalid amount of arguments passed to script")

#sys.argv[1]
print(find_char(sys.argv[1]))
dic1 = json.dumps(find_char(sys.argv[1]))
print(dic1)
to_file(dic1)

