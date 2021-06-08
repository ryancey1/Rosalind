#! /usr/bin/env python3

'''
Reading and Writing Problem
Given: A file containing at most 1000 lines.
Return: A file containing all the even-numbered lines from the original file. Assume 1-based numbering of lines.
'''

import sys

# f = sys.argv[1]
f = './rosalind_ini5.txt'
file = open(f)
i = 1
evens = ''


for line in file:
    if i < 1000 and i % 2 == 0:
        print(line.rstrip('\n'))
        i += 1
    elif i > 1000:
        print('Too many lines in this file.')
        sys.exit()
    else:
        i += 1

print(evens)