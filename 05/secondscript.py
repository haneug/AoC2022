#!/usr/bin/python

file = open('input.txt','r')
lines = file.read().splitlines()

stacks=[[],[],[],[],[],[],[],[],[]]
for line in lines:
    if line.split()[0] == '1':
        procedure=lines[lines.index(line)+2:len(lines)]
        break
    for i in range(0,9):
        crate=line[1+i*4]
        if crate != " ":
            stacks[i].insert(0,crate)

print(stacks) 
for line in procedure:
   number=int(line.split()[1]) 
   origin=int(line.split()[3]) 
   target=int(line.split()[5])
   stacks[target-1] = stacks[target-1] + stacks[origin-1][-number:]
   stacks[origin-1] = stacks[origin-1][:-number]

for stack in stacks:
    print(stack[-1],end='')
