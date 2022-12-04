#!/usr/bin/python

def compare(a,b,c,d):
    for i in range(a,b+1):
        if i in range(c,d+1):
            return True
    return False

file = open('input.txt','r')
lines = file.read().splitlines()

sum = 0

for line in lines:
    elv1start=int(line.split(',')[0].split('-')[0])
    elv1end=int(line.split(',')[0].split('-')[1])
    elv2start=int(line.split(',')[1].split('-')[0])
    elv2end=int(line.split(',')[1].split('-')[1])
    #print(elv1start,elv1end,elv2start,elv2end)
    if compare(elv1start,elv1end,elv2start,elv2end):
        sum += 1

print(sum)
