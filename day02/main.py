#!/usr/bin/env python3

aim = 0
answer = 0
position = 0
depth = 0

file = open('input.txt', 'r').read().splitlines()

for line in file:
    if(line.find('down') != -1):
        aim += int(line.split('down ')[1])
    elif(line.find('up') != -1):
        aim -= int(line.split('up ')[1])
    elif(line.find('forward') != -1):
        position += int(line.split('forward ')[1])
        depth += aim * int(line.split('forward ')[1])

answer = position * depth
print('Answer:', answer)
