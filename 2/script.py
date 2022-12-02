#!/usr/bin/python

shp={"X": 1, "Y": 2, "Z": 3}
ohp={"A": 1, "B": 2, "C": 3}
file = open('input.txt','r')
lines = file.read().splitlines()

points = 0

for line in lines:
    op = ohp[line.split()[0]]
    my = shp[line.split()[1]]
    points += my
    if op == my:
        points += 3
        continue
    elif (my == 1 and op == 2):
        points += 0
        continue
    elif (my == 1 and op == 3):
        points += 6
        continue
    elif (my == 2 and op == 3):
        points += 0
        continue
    elif (my == 2 and op == 1):
        points += 6
        continue
    elif (my == 3 and op == 1):
        points += 0
        continue
    elif (my == 3 and op == 2):
        points += 6
        continue

print(points)
