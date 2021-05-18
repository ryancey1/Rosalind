#! /usr/bin/env python3

'''
Conditions and Loops Problem
Given: Two positive integers a and b (a<b<10000).
Return: The sum of all odd integers from a through b, inclusively.
'''

import sys

args = sys.argv

a = int(args[1])
b = int(args[2])

sum = 0

for number in range(a, b):
    if number % 2 != 1:
        number += 1
    else:
        sum += number
        number += 1

print(f'{sum}')