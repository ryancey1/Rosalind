#! /usr/bin/env python3

import sys

# dna = 'GATGGAACTTGACTACGTAAATT'
seq = open(sys.argv[1])
dna = seq.read().rstrip('\n')

rna = ''

for base in dna:
    if base == 'T':
        rna += 'U'
    else:
        rna += base

print(rna)