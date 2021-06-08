#! /usr/bin/env python3

'''
Given: A collection of DNA strings in FASTA format having total length at most 10 kbp.
Return: The adjacency list corresponding to O(3). You may return edges in any order.
'''

import bioinformatics_tools as bfx
import sys

def adjacency_list(seqs, k = 3):
    adj = []
    for key1, s in seqs.items():
        for key2, t in seqs.items():
            a, b = list(seqs.keys()).index(key1), list(seqs.keys()).index(key2)
            if b == a:
                continue
            elif s[-k:] == t[0:k]:
                adj.append(f'{key1} {key2}')
    return adj
                


if __name__ == '__main__':
    fasta_file = sys.argv[1]
    # fasta_file = '/Users/ryanyancey/Git/Rosalind/Bioinformatics-Stronghold/rosalind_grph.txt'
    seqs = bfx.read_fasta_dict(fasta_file)
    adj = adjacency_list(seqs)
    for a in adj:
        print(a)

