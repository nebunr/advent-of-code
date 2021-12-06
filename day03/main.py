#!/usr/bin/env python3

from enum import Enum

class Rating(Enum):
    OXYGEN = 1
    CO2 = 2

def part1():
    count = [0,0,0,0,0,0,0,0,0,0,0,0]
    gamma = [0,0,0,0,0,0,0,0,0,0,0,0]
    epsilon = [0,0,0,0,0,0,0,0,0,0,0,0]
    file = open('input.txt', 'r').read().splitlines()
    for line in file:
        result = []
        for i in range(0, len(line), 1):
            result.append(int(line[i : i + 1]))
        for i in range(len(result)):
            if int(result[i]) == 1:
                count[i] += 1
            elif int(result[i]) == 0:
                count[i] -= 1
    for i in range(len(count)):
        if count[i] >= 0:
            gamma[i] = 1
            epsilon[i] = 0
        else:
            gamma[i] = 0
            epsilon[i] = 1
    # Binary to Decimal
    answer = int("".join(str(i) for i in gamma), 2)
    answer *= int("".join(str(i) for i in epsilon), 2)
    print('Part 1:', answer)

def part2():
    lines = []
    with open('input.txt', 'r') as file:
        while line := file.readline().rstrip():
            lines.append(line)
    oxygen = rating(lines, Rating.OXYGEN)
    co2 = rating(lines, Rating.CO2)
    print(oxygen * co2)

def rating(lines, rating):
    i = 0
    while len(lines) > 1:
        count = 0
        for j in range(0, len(lines)):
            count += int(lines[j][i])
        remove = []
        for line in lines:
            if bit_criteria(count, len(lines), rating) != int(line[i]):
                remove.append(line)
        lines = list(set(lines) - set(remove))
        i += 1
    return int("".join(str(i) for i in lines[0]), 2)

def bit_criteria(count, total, rating):
    if rating == Rating.OXYGEN:
        if count >= total / 2:
            return 1
        else:
            return 0
    else: # rating == Rating.CO2
        if count >= total / 2:
            return 0
        else:
            return 1

if __name__ == "__main__":
    part1()
    part2()
