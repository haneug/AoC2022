#!/usr/bin/python

def check_pos(pos,a,b,c,d):
    if [a+c,b+d] in pos: return pos
    if a+c < 0: return pos
    if a+c >= len(grid): return pos
    if b+d < 0: return pos
    if b+d >= len(grid[a+c]): return pos
    #print("{} {} {} {} {} {}".format(a,b,c,d,grid[a+c][b+d],grid[a][b]))
    if (ord(grid[a+c][b+d])-ord(grid[a][b])) <= 1:
        pos.append([a+c,b+d])
    return pos

def eval_dir(pos):
    for i in range(len(pos)):
        #if i >= len(pos): break
        #UP
        pos=check_pos(pos,pos[i][0],pos[i][1],-1,0)
        #DOWN
        pos=check_pos(pos,pos[i][0],pos[i][1],1,0)
        #RIGHT
        pos=check_pos(pos,pos[i][0],pos[i][1],0,1)
        #LEFT
        pos=check_pos(pos,pos[i][0],pos[i][1],0,-1)
    return pos

file = open('input.txt','r')
lines = file.read().splitlines()

grid = [[ x for x in line ] for line in lines ]

# Lets find the start
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == "S":
            print("S is at position {} {}".format(i,j))
            start = [i,j]
            grid[start[0]][start[1]] = "a"
        if grid[i][j] == "E":
            print("E is at position {} {}".format(i,j))
            end = [i,j]
            grid[end[0]][end[1]] = "z"

position = [start]
sum=0
while True:
    position = eval_dir(position)
    sum+=1
    if end in position:
        break
    else:
        continue
    break

print("The shortest pathway from S takes {} steps".format(sum))


position=[]

# Lets find the start
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == "a":
            position.append([i,j])

sum=0
while True:
    position = eval_dir(position)
    sum+=1
    if end in position:
        break
    else:
        continue
    break

print("The shortest pathway from any a takes {} steps".format(sum))
