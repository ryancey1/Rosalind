#! /usr/bin/env python3

'''
Complementing a Strand of DNA Problem

Given: A DNA string s of length at most 1000 bp.

Return: The reverse complement s.
'''

import sys
import bioinformatics_tools as bfx

file = sys.argv[1]
dna = bfx.read_fasta(file)

for seq in dna:
    print(bfx.reverse_complement(seq))