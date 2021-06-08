#! /usr/bin/env python3

'''
'''

import sys
import bioinformatics_tools as bfx

# reads sequences into a list and checks if the number of sequences is correct
def import_seqs(file):
    with open(file) as f:
        return [line.strip() for line in f]


if __name__ == '__main__':
    # file = sys.argv[1]
    file = 'rosalind_hamm.txt'
    seqs = import_seqs(file)
    
    seq1, seq2 = seqs[0], seqs[1]

    hd = bfx.hamming_distance(seq1, seq2)
    print(hd)