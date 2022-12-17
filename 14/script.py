#!/usr/bin/python3

file = open('input.txt', 'r')
lines = file.read().splitlines()

stones = []


def sand_falling(pos, obj, low):
    if pos in obj: return
    while pos[1] < low:
        if pos[1] + 1 == floor:
            obj.append(pos)
            return
        # check down
        if [pos[0], pos[1] + 1] in obj:
            # check left
            if [pos[0] - 1, pos[1] + 1] in obj:
                #  check right
                if [pos[0] + 1, pos[1] + 1] in obj:
                    obj.append(pos)
                    return
                else:
                    pos[0] += 1
                    pos[1] += 1
                    continue
            else:
                pos[0] -= 1
                pos[1] += 1
                continue
        else:
            pos[1] += 1
            continue


def stone_gen(a, b):
    tmp = []
    if a[0] == b[0]:
        if a[1] < b[1]:
            for j in range(a[1], b[1] + 1):
                tmp.append([a[0], j])
        else:
            for j in range(b[1], a[1] + 1):
                tmp.append([a[0], j])
    else:
        if a[0] < b[0]:
            for j in range(a[0], b[0] + 1):
                tmp.append([j, a[1]])
        else:
            for j in range(b[0], a[0] + 1):
                tmp.append([j, a[1]])
    return tmp


for line in lines:
    line = line.split()
    pathway = []
    for i in range(0, len(line), 2):
        pathway.append(line[i])
    for i in range(0, len(pathway) - 1):
        start = [int(x) for x in pathway[i].split(',')]
        end = [int(x) for x in pathway[i + 1].split(',')]
        # print(start, end)
        stones = stones + stone_gen(start, end)

number_stones = len(stones)
objects = stones
lowest_stone = max(stone[-1] for stone in stones)
floor = lowest_stone + 2
old = len(objects)

while True:
    sand_falling([500, 0], objects, lowest_stone)
    if old < len(objects):
        old = len(objects)
    else:
        break

sand = old - number_stones
print("The remaining sand is {}".format(sand))

objects = stones
old = len(objects)
while True:
    sand_falling([500, 0], objects, floor)
    if old < len(objects):
        old = len(objects)
    else:
        break

sand = old - number_stones
print("The remaining sand with floor is {}".format(sand))
