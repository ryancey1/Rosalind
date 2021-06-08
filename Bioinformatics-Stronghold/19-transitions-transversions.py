#! /usr/bin/env python3

'''

'''

import sys, bioinformatics_tools as bfx

if __name__ == '__main__':
    file = '/Users/ryanyancey/Git/Rosalind/Bioinformatics-Stronghold/rosalind_tran.txt'
    # file = sys.argv[1]
    fasta = bfx.read_fasta(file)
    query = [v for v in fasta.values()]
    print(bfx.transitions_transversions(query[0], query[1]))
