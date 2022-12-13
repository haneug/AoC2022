#!/usr/bin/python

def movetail(tail,distance):
    if distance == [2,0]:
        tail[0]+=1
    if distance == [-2,0]:
        tail[0]-=1
    if distance == [0,2]:
        tail[1]+=1
    if distance == [0,-2]:
        tail[1]-=1
    if distance == [1,2] or distance == [2,1] or distance == [2,2]:
        tail[0], tail[1] = tail[0]+1,tail[1]+1
    if distance == [1,-2] or distance == [2,-1] or distance == [2,-2]:
        tail[0], tail[1] = tail[0]+1,tail[1]-1
    if distance == [-1,2] or distance == [-2,1] or distance == [-2,2]:
        tail[0], tail[1] = tail[0]-1,tail[1]+1
    if distance == [-1,-2] or distance == [-2,-1] or distance == [-2,-2]:
        tail[0], tail[1] = tail[0]-1,tail[1]-1
    return tail

def dist(list1,list2):
    return [x - y for x,y in zip(list1,list2)]

def move(rope,dir,length):
    if dir == "R":
        step=[1,0]
        for _ in range(length): 
            rope[0] = [x + y for x, y in zip(rope[0], step)]
            for i in range(len(rope)-1):
                distance=dist(rope[i],rope[i+1])
                rope[i+1]=movetail(rope[i+1],distance)
            been.add(tuple(rope[-1]))
    elif dir == "L":
        step=[-1,0]
        for _ in range(length): 
            rope[0] = [x + y for x, y in zip(rope[0], step)]
            for i in range(len(rope)-1):
                distance=dist(rope[i],rope[i+1])
                rope[i+1]=movetail(rope[i+1],distance)
            been.add(tuple(rope[-1]))
    elif dir == "U":
        step=[0,1]
        for _ in range(length): 
            rope[0] = [x + y for x, y in zip(rope[0], step)]
            for i in range(len(rope)-1):
                distance=dist(rope[i],rope[i+1])
                rope[i+1]=movetail(rope[i+1],distance)
            been.add(tuple(rope[-1]))
    elif dir == "D":
        step=[0,-1]
        for _ in range(length): 
            rope[0] = [x + y for x, y in zip(rope[0], step)]
            for i in range(len(rope)-1):
                distance=dist(rope[i],rope[i+1])
                rope[i+1]=movetail(rope[i+1],distance)
            been.add(tuple(rope[-1]))
    return rope
                                   
file = open('input.txt','r')
lines = file.read().splitlines()

startrope=[[0,0],[0,0]]
distance=[0,0]
been={(0,0)}

for line in lines:
    direction=line.split()[0]
    length=int(line.split()[1])
    startrope=move(startrope,direction,length)


print("The tail visited {} unique positions".format(len(been))) 

longrope=[[0,0] for i in range(10)]
distance=[0,0]
been={(0,0)}

for line in lines:
    direction=line.split()[0]
    length=int(line.split()[1])
    longrope=move(longrope,direction,length)

print("The tail of the long rope visited {} unique positions".format(len(been))) 
