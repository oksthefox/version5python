#!/usr/bin/python3

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = 4


def binary_search(list, target):
    left = 0
    right = len(list)-1
    while left<=right:
        mid = (left+right)//2
        if list[mid]==target:
            return mid
        elif list[mid]<target:
            left = mid +1
        else:
            right = mid -1
    return -1
print(binary_search(a,b))

result = binary_search(a,b)
if result != -1:
    print("Target value found in the list")
else:
    print("Target value not found in the list")