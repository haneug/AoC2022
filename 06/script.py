#!/usr/bin/python

def check(list):  
    if len(set(list)) == len(list): return True

file = open('input.txt','r')
buffer = file.read().splitlines()[0]

seq = []
mes = []

for i in range(len(buffer)):
    if len(seq) < 5: seq.append(buffer[i])
    if len (seq) == 4: 
        if check(seq): 
            print("Found the first marker after {} characters.".format(i+1))
            break
        seq.pop(0)

for i in range(len(buffer)):
    if len(mes) < 15: mes.append(buffer[i])
    if len(mes) == 14:
        if check(mes): 
            print("Found the first message marker after {} characters.".format(i+1))
            break
        mes.pop(0)
