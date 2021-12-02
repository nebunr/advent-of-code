#!/usr/bin/env python3

# Part 1
depth = []
file = open('input.txt', 'r').read().splitlines()

for line in file:
    depth.append(int(line))

count = 0
for i in range(len(depth)):
    if i > 0:
        if (depth[i] - depth[i-1]) > 0:
            count += 1
print('Part 1:', count)

# Part 2
window = []
for i in range(len(depth)-2):
    window.append(depth[i] + depth[i+1] + depth[i+2])

count = 0
for i in range(len(window)):
    if i > 0:
        if (window[i] - window[i-1]) > 0:
            count += 1
print('Part 2:', count)
