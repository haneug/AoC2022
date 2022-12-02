#!/usr/bin/python

shp={"X": 1, "Y": 2, "Z": 3}
ohp={"A": 1, "B": 2, "C": 3}
file = open('input.txt','r')
lines = file.read().splitlines()

points = 0

for line in lines:
    op = ohp[line.split()[0]]
    my = shp[line.split()[1]]
    #loose
    if my == 1:
        tmp = (op-1)
        if tmp == 0:
            tmp = 3
        print(op,my)
        print("loose:", (tmp))
        points += tmp
    #draw
    elif my == 2:
        print(op,my)
        print("draw:", (op+3))
        points += (op + 3)
    #win
    elif my == 3:
        print(op,my)
        print("win:", (op%3 + 7))
        points += (op%3 + 7)

print(points)
