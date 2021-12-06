#!/usr/bin/env python3

class Calcuations:
    aim = 0
    position = 0
    depth = 0

p1 = Calcuations()
p2 = Calcuations()

for line in open('input.txt', 'r').read().splitlines():
    if(line.find('down') != -1):
        p1.depth += int(line.split('down ')[1])
        p2.aim += int(line.split('down ')[1])
    elif(line.find('up') != -1):
        p1.depth -= int(line.split('up ')[1])
        p2.aim -= int(line.split('up ')[1])
    elif(line.find('forward') != -1):
        p1.position += int(line.split('forward ')[1])
        p2.position += int(line.split('forward ')[1])
        p2.depth += p2.aim * int(line.split('forward ')[1])

print('Part 1:', p1.position * p1.depth)
print('Part 2:', p2.position * p2.depth)
