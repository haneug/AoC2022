#!/usr/bin/python

def compare(a,b):
    for i in a:
        if i in b:
            return i

file = open('input.txt','r')
lines = file.read().splitlines()

prio=list(map(chr, range(ord('a'), ord('z')+1)))+list(map(chr, range(ord('A'), ord('Z')+1)))

sum = 0
for line in lines:
    first=line[0:len(line)/2]
    second=line[len(line)/2:len(line)]
    #print(first,second)
    match=compare(first,second)
    #print(match,prio.index(match)+1)
    sum += prio.index(match)+1
print(sum)
