#!/usr/bin/python

def evaluate(index):
    if index not in size:
        size[index] = 0
    for i in folders[index]:
        if i.split()[0] == "dir":
            size[index] += evaluate(index+ "/"+ i.split()[1])
        else:
            size[index] += int(i.split()[0])
    return size[index]


wdir=['/']
folders={}
size={}
totmem=70000000
reqmem=30000000

file = open('input.txt','r')
lines = file.read().splitlines()


for i in range(len(lines)):
    #print("lines:" +  lines[i])
    if lines[i].split()[1] == 'cd':
        if lines[i].split()[2] == "..":
            wdir.pop()
        elif lines[i].split()[2] != "/":
            wdir.append(lines[i].split()[2])
        if lines[i].split()[2] == "/":
            wdir=['/']
        #print(wdir)
    if lines[i].split()[1] == "ls":
        tmplist=[]
        i += 1
        while ((lines[i].split()[0] != "$")): 
            tmplist.append(lines[i])
            #print(tmplist)
            folders["/".join(wdir)]=tmplist
            i += 1
            #print(i)
            if i >= len(lines): break

#print(folders)

#Evaluate
occmem=evaluate('/')
print("The total occupied size of the system is {}.".format(occmem))

tofree=reqmem-(totmem-occmem)

sum=0
for i in size:
    if size[i] <= 100000:
        sum += size[i]

print("The sum of all folders with total size smaller 100000 is {}.".format(sum))

target=occmem
for i in size:
    if size[i] >= tofree and (size[i] < target):
        target=size[i]

print("The size of the smallest directory that frees enugh space for the update is {}.".format(target))



