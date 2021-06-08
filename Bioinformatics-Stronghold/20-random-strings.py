#! /usr/bin/env python3

'''

'''

import math
import sys

# file = sys.argv[1]
file = '/Users/ryanyancey/Git/Rosalind/Bioinformatics-Stronghold/rosalind_prob.txt'
info = open(file).readlines()
dna = info[0].rstrip('\n')
A = info[1].rstrip('\n').split()
B = ''

for gc in A:
    g_or_c = float(gc)/2
    a_or_t = (1-float(gc))/2
    prob = 1.0

    for nt in dna:
        if nt == 'A' or nt == 'T':
            prob *= a_or_t
        else:
            prob *= g_or_c
    Bk = round(math.log10(prob), 3)
    B += f'{Bk} '

print(B)
