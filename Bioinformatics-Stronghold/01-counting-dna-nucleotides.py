#! /usr/bin/env python3

'''
Counting DNA Nucleotides Problem
Given: A DNA string s of length at most 1000 nt.
Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.
'''

import sys


nt = {}
bases = ['A', 'C', 'G', 'T']
count = ''

seq = open(sys.argv[1])
dna = seq.read()

# dna = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'

for bp in dna:
    nt[bp] = nt.get(bp, 0) + 1

for base in bases:
    count += str(nt.get(base)) + " "

print(count)