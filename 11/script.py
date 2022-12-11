#!/usr/bin/python

import operator

operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '**': operator.pow,
    '/': operator.truediv
}

class Monkey:
    def __init__(self,items,symbol,integer,test):
        self.items = items
        self.op = operators.get(symbol)
        self.int = integer
        self.div = test[0]
        self.true = test[1]
        self.false = test[2]
        self.count = 0

    def inspect(self):
        self.items[0] = self.op(self.items[0], self.int)
        self.count += 1

    def bored(self):
        self.items[0] = self.items[0] / 3

    def test(self,monkeys):
        self.items[0] %= N
        if self.items[0] % self.div == 0:
            #print("Throwing to Monkey {}".format(self.true))
            monkeys[self.true].items.append(self.items.pop(0))
        else:
            #print("Throwing to Monkey {}".format(self.false))
            monkeys[self.false].items.append(self.items.pop(0))

file = open('input.txt','r')
lines = file.read().splitlines()

monkeys = []
N = 1

for i in range(0,len(lines),7):
    items = lines[i+1].split()[2:]
    intitems = [eval(x.strip(",")) for x in items]
    operation = lines[i+2].split()[4]
    integer = lines[i+2].split()[5]
    if operation == "*" and integer == "old":
        operation = "**"
        integer = "2"
    integer = int(integer)
    test1 = int(lines[i+3].split()[-1])
    N *= test1
    test2 = int(lines[i+4].split()[-1])
    test3 = int(lines[i+5].split()[-1])
    monkeys.append(Monkey(intitems,operation,integer,[test1,test2,test3]))

for i in range(20):
    for monkey in monkeys:
        for _ in range(len(monkey.items)):
            monkey.inspect()
            monkey.bored()
            monkey.test(monkeys)

counter = [monkey.count for monkey in monkeys]
counter.sort()

buisness=counter[-1]*counter[-2]

print("The level of monkey buisness is {}".format(buisness))

monkeys = []

for i in range(0,len(lines),7):
    items = lines[i+1].split()[2:]
    intitems = [eval(x.strip(",")) for x in items]
    operation = lines[i+2].split()[4]
    integer = lines[i+2].split()[5]
    if operation == "*" and integer == "old":
        operation = "**"
        integer = "2"
    integer = int(integer)
    test1 = int(lines[i+3].split()[-1])
    test2 = int(lines[i+4].split()[-1])
    test3 = int(lines[i+5].split()[-1])
    monkeys.append(Monkey(intitems,operation,integer,[test1,test2,test3]))

for i in range(10000):
    for monkey in monkeys:
        for _ in range(len(monkey.items)):
            monkey.inspect()
            monkey.test(monkeys)


counter = [monkey.count for monkey in monkeys]
counter.sort()

buisness=counter[-1]*counter[-2]

print("The level of monkey buisness without relief is {}".format(buisness))

