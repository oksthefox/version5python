#!/usr/bin/python3
import os
import sys
import csv
import hashlib


def recursive_list(direct):

    if os.path.exists(direct):
        print("the directory exists")
        for root, dirs, files in os.walk(direct):
            for file in files:
                path = os.path.join(root,file)
                print (path)

    else:
        print("the directory does not exist")

recursive_list(sys.argv[1])

def recursive_listV2(direct):

    with open ("file.csv","w") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['number','file_path','md5'])
        count = 0
        for root, dirs, files in os.walk(direct):
            for file in files:
                count+=1
                with open (file, 'rb') as filename:
                    data= filename.read()
                path = os.path.join(root,file)
                writer.writerow([count, path, hashlib.md5(data).hexdigest() ])
recursive_listV2(sys.argv[1])

