#!/usr/bin/python

def compare(a,b,c,d):
    if (a == c and b == d):
        #print('elv1 and elv2 are equl')
        return True
    elif (a >= c and b <= d):
        #print('elv1 included in elv2')
        return True
    elif (c >= a and d <= b):
        #print('elv2 included in elv1')
        return True
    else:
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
