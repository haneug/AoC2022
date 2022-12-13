#!/usr/bin/python

def compare(a,b,c):
    for i in a:
        if i in b:
            if i in c:
                return i

file = open('input.txt','r')
lines = file.read().splitlines()

prio=list(map(chr, range(ord('a'), ord('z')+1)))+list(map(chr, range(ord('A'), ord('Z')+1)))

sum = 0
for i in range(0,len(lines),3):
    match=compare(lines[i],lines[i+1],lines[i+2])
    print(match,prio.index(match)+1)
    sum += prio.index(match)+1
print(sum)
