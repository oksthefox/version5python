#!/usr/bin/python3
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 55, 89]

def newlist(list):
    the_list =[]
    for x in list:
        if x in the_list:
            continue
        else:
            the_list.append(x)
    return the_list


print("This is the new list: ")
print(newlist(a))
