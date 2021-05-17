#! /usr/bin/env python3

'''
Strings and Lists Problem
Given: A string s of length at most 200 letters and four integers a, b, c and d.
Return: The slice of this string from indices a through b and c through d (with space in between), inclusively. In other words, we should include elements s[b] and s[d] in our slice.
'''

import sys

args = sys.argv

s = args[1]

if len(s) > 2000:
    print('String must be less than 2000 characters.')
    sys.exit

cut1 = int(args[2])
cut2 = int(args[3]) + 1

cut3 = int(args[4])
cut4 = int(args[5]) + 1

print(f'{s[cut1:cut2]} {s[cut3:cut4]}')
