#!/usr/bin/python3
import re
import sys
import os



#file = sys.argv[1]
#with open (file, 'r') as f:
#    for line in f:
#        if re.search('test',line):
#            print(line.strip())

if len(sys.argv) == 3:
    word = sys.argv[1]
    file = str(sys.argv[2])
    if os.path.exists(file):
        print("the file "+ file+ " is exists")
        with open (file, 'r') as f:
            for line in f:
                if re.search(word,line):
                    print(line.strip())
    else:
        print("the file "+file+" doesn't exist")
else:
    print("invalid amount of arguments passed to script")
