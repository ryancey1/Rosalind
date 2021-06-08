#! /usr/bin/env python3

'''

'''

import re
import sys
import bioinformatics_tools as bfx


def main():
    try:
        file = sys.argv[1]
    except (IndexError):
        file = '/Users/ryanyancey/Git/Rosalind/Bioinformatics-Stronghold/rosalind_orf.txt'
    dna = bfx.read_fasta(file)

    if len(dna) > 1000:
        sys.exit('Imported DNA is longer than 1kbp.')

    orfs = []
    for x in dna.values():
        orfs += bfx.find_orfs(x)

    proteins = [bfx.translate_rna_protein(x) for x in orfs]
    proteins = set([''.join(aa) for aa in proteins])
    print(*sorted(proteins, key=len, reverse=True), sep='\n')


if __name__ == '__main__':
    main()
