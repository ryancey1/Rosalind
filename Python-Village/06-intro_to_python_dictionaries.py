#! /usr/bin/env python3

'''
Intro to Python Dictionaries Problem
Given: A string s of length at most 10000 letters.
Return: The number of occurrences of each word in s, where words are separated by spaces. Words are case-sensitive, and the lines in the output can be in any order.
'''

import sys

dictionary = {}
string = open(sys.argv[1]).read()
list = string.split()

for item in list:
    dictionary[item] = dictionary.get(item, 0) + 1

for key, value in dictionary.items():
    print(f'{key} {value}')