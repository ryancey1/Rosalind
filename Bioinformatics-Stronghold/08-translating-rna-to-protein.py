#! /usr/bin/'env': 'python3',

'''
'''

import sys
import bioinformatics_tools as bfx

if __name__ == '__main__':
    file = sys.argv[1]
    # file = '/Users/ryanyancey/Git/Rosalind/Bioinformatics-Stronghold/rosalind_prot.txt'
    rna = open(file).read().rstrip('\n').rstrip()
    bfx.translate_rna_protein(rna)