#! /usr/bin/env python3

'''
'''

import sys

# reads sequences into a list and checks if the number of sequences is correct
def import_seqs(file):
    seqs = []
    while True:
        line = file.readline().rstrip('\n')
        if not line or line == '':
            break
        seqs.append(line)
    if len(seqs) > 2:
        exit('Error: Number of sequences cannot exceed 2')
    return seqs        


file = open(sys.argv[1])
seqs = import_seqs(file)

seq1, seq2 = seqs[0], seqs[1]
len1, len2 = len(seq1), len(seq2)

hd = 0

for i in range(len(seq1)):
    s, t = seq1[i], seq2[i]
    if s != t:
        hd += 1

print(hd)