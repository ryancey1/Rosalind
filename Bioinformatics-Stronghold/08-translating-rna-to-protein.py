#! /usr/bin/'env': 'python3',

'''
'''

import sys, os
import bioinformatics_tools as bfx

if __name__ == '__main__':
    # file = sys.argv[1]
    file = os.getcwd() + '/Bioinformatics-Stronghold/rosalind_prot.txt'
    rna = bfx.read_fasta(file)
    for orf in rna:      
        print(bfx.translate_rna_protein(orf))
        