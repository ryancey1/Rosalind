#! /usr/bin/env python3

'''
'''

import sys

import bioinformatics_tools as bfx


def lcs(fasta):
    fasta = sorted(fasta, key = len)
    shortest = fasta[0]
    comps = fasta[1:]
    motif = ''
    for nt_start in range(len(shortest)):
        for nt_end in range(nt_start+1, len(shortest)):
            m = shortest[nt_start:nt_end]
            found = False
            for seqs in comps:
                if m in seqs:
                    found = True
                else:
                    found = False
                    break
            if found and len(m) > len(motif):
                motif = m
    print(motif)


if __name__ == '__main__':
    file = '/Users/ryanyancey/Git/Rosalind/Bioinformatics-Stronghold/rosalind_lcsm.txt'
    # file = sys.argv[1]
    fasta = bfx.read_fasta(file)
    lcs(fasta)
