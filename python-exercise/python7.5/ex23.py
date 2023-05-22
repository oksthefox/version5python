#!/usr/bin/python3
import sys

def overlap (file1, file2):
    try:
        with open (file1, 'r') as f1:
            data1 = f1.read().split(',')
            with open(file2, 'r') as f2:
                data2 = f2.read().split(',')
                lst = []
                for x in data1:
                    if x in data2:
                        lst.append(x)
                print(lst)
    except:
        print ("wrong useage!")

overlap(sys.argv[1],sys.argv[2])
