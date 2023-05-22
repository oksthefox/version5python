#!/usr/bin/python3
x = "oksana"
print(x.upper())
print(x[::-1])
print(len(x))
mid_x = len(x) // 2 
#print(x.replace(str(mid_x),"*"))
new_x = x[:mid_x] + "*" + x[mid_x+1:]
print(new_x)
