#! /usr/bin/env python3

'''
Variables and Some Arithmetic Problem
Given: Two positive integers a and b, each less than 1000.
Return: The integer corresponding to the square of the hypotenuse of the right triangle whose legs have lengths a and b.
'''

import sys

a = int(sys.argv[1])
b = int(sys.argv[2])

if a > 1000 or b > 1000:
    print('Both input integers must be less than 1000.')
    sys.exit


## a^2 + b^2 = c^2

c2 = a*a + b*b
print(c2)
