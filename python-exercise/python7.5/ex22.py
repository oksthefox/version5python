#!/usr/bin/python3

import sys
def list(file):
    dic={}
    try:
        with open (file,"r") as file:
            names = file.read().split()
            for x in names:
                if x in dic:
                    dic[x]+=1
                else:
                    dic[x]=1
    except:
        print("the file donwt exist.")
        
    return dic
    
    
print (dic(sys.argv[1]))    