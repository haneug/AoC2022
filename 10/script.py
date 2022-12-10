#!/usr/bin/python


def cycle_iter(cycle,crt,x,target):
    sprite=[x-1,x,x+1]
    if crt%40 in sprite:
        image.append("#")
    else:
        image.append(".")
    cycle+=1
    crt+=1
    if cycle in target:
        signal.append(cycle*x)
    return cycle,crt

file = open('input.txt','r')
lines = file.read().splitlines()

target=[i for i in range(20,260,40)]
image=[]
signal=[]
cycle=0
x=1
crt=0

for line in lines:
    if line.split()[0] == "addx":
        cycle, crt = cycle_iter(cycle,crt,x,target)
        cycle, crt = cycle_iter(cycle,crt,x,target)
        x+=int(line.split()[1])
    elif line.split()[0] == "noop":
        cycle, crt = cycle_iter(cycle,crt,x,target)

print("The signal strength is {}".format(sum(signal)))

for i in range(6):
    line=image[0+i*40:40+i*40]
    print("".join(line))
