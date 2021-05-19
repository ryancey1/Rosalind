#! /usr/bin/env python3

'''
Complementing a Strand of DNA Problem
Given: A DNA string s of length at most 1000 bp.
Return: The reverse complement s.
'''

import sys

dna = open(sys.argv[1]).read().rstrip('\n')

reverse = ''
for base in dna:
    reverse = base + reverse

complement = reverse.lower()
complement = complement.replace('a', 'T')
complement = complement.replace('t', 'A')
complement = complement.replace('c', 'G')
complement = complement.replace('g', 'C')

print(complement)