#!/usr/bin/python

def check(l, r):
    # Case both are integers
    if isinstance(l, int) and isinstance(r, int):
        # print("{} and {} are integers".format(l,r))
        if l > r:
            # print("wrong order found for {} and {}".format(l,r))
            return "Wrong"
        elif l < r:
            # print("right order found for {} and {}".format(l,r))
            return "Right"
        else:
            # print("Continue because no winner found for {} and {}".format(l,r))
            return ""
    # Case both are lists
    elif isinstance(l, list) and isinstance(r, list):
        # print("{} and {} are lists".format(l,r))
        try:
            _ = 0
            while True:
                # print("list entries {} and {} are checked".format(l[_],r[_]))
                test = check(l[_], r[_])
                if test == "":
                    _ += 1
                    continue
                else:
                    return test
        except:
            if len(l) > len(r):
                # print("wrong order found for {} and {}".format(l,r))
                return "Wrong"
            elif len(l) < len(r):
                # print("right order found for {} and {}".format(l,r))
                return "Right"
            else:
                # print("Continue because no winner found for {} and {}".format(l,r))
                return ""
    # Case one has to be integer
    else:
        # print("{} and {} are a list and an integer".format(l,r))
        if isinstance(l, int):
            # print("Converting {} to list {}".format(l,l))
            l = [l]
            test = check(l, r)
            return test
        else:
            # print("Converting {} to list {}".format(r,r))
            r = [r]
            test = check(l, r)
            return test


file = open('input.txt', 'r')
lines = file.read().splitlines()

sum = 0
for i in range(0, len(lines), 3):
    left = eval(lines[i])
    right = eval(lines[i + 1])
    # print("{} vs. {}".format(left,right))
    test = check(left, right)
    if test == "Right":
        # print("correct order in index {} !".format(i/3+1))
        sum += i / 3 + 1

print("The sum of the indexes with the correct order is {}".format(sum))

start = [[2]]
end = [[6]]

print(start[-1])
print(end[-1])
for line in lines:
    if line == "": continue
    left = eval(line)
    test = check(left, start[-1])
    if test == "Right":
        start.insert(0, left)
    test = check(left, end[-1])
    if test == "Right":
        end.insert(0, left)

print("The index number of the seperator are {} and {}".format(len(start), len(end) + 1))
print("The decoder is {}".format(len(start) * (len(end) + 1)))
