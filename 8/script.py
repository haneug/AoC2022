#!/usr/bin/python

file = open('input.txt','r')
lines = file.read().splitlines()

grid=[]

for line in lines:
    tmplist=[]
    for letter in line:
        tmplist.append(letter)
    grid.append(tmplist)

sum=0
maxscore=0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        right=True
        left=True
        up=True
        down=True
        nright=0
        nleft=0
        nup=0
        ndown=0
        for k in range(i-1,-1,-1):
            nup+=1
            if grid[i][j] <= grid[k][j]: 
                up=False
                break
        for k in range(i+1,len(grid)):
            ndown+=1
            if grid[i][j] <= grid[k][j]: 
                down=False
                break
        for k in range(j+1,len(grid[i])):
            nright+=1
            if grid[i][j] <= grid[i][k]:
                right=False
                break
        for k in range(j-1,-1,-1):
            nleft+=1
            if grid[i][j] <= grid[i][k]:
                left=False
                break
        if (right) or (left) or (up) or (down):
            sum+=1
        score=nup*ndown*nright*nleft
        if score > maxscore: maxscore = score

print("Number of visible trees is {}".format(sum))
print("The maximum score is {}".format(maxscore))


            
