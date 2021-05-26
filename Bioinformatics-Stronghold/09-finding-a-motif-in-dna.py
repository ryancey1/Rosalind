#! /usr/bin/env python3

'''
Given: Two DNA strings s and t (each of length at most 1 kbp).

Return: All locations of t as a substring of s.
'''

import sys, re

def find_substrings(string, motif):
    start_indices = ''
    for i in range(len(string)):
        start, end = i, i+len(motif)
        if motif in string[start:end]:
            start_indices += f'{start+1} '
    if start_indices == '':
        print('No matches.')
    else:
        print(start_indices)

if __name__ == '__main__':
    file = open(sys.argv[1])
    s = file.readline().rstrip('\n')
    t = file.readline().rstrip('\n')
    find_substrings(s, t)