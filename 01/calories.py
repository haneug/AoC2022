#!/usr/bin/python

file = open('input.txt','r')
lines = file.read().splitlines()

tmp = 0
max = 0
for i in lines:
    if i == "":
        if tmp > max:
            max=tmp
        tmp = 0
    else:
        tmp += int(i)

print(max)
    
