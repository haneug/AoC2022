#!/usr/bin/python

file = open('input.txt','r')
lines = file.read().splitlines()

tmp = 0
first = 0
second = 0
third = 0
for i in lines:
    if i == "":
        if tmp > first:
            third = second
            second = first
            first = tmp
        elif tmp > second:
            third = second
            second = tmp
        elif tmp > third:
            third = tmp
        tmp = 0
    else:
        tmp += int(i)

print(first+second+third)
    
