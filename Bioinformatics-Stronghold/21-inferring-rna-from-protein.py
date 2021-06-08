#! /usr/bin/env python3

'''
'''

import sys
from bioinformatics_tools import infer_rna


def main():
    try:
        file = sys.argv[1]
    except (IndexError):
        file = '/Users/ryanyancey/Git/Rosalind/Bioinformatics-Stronghold/rosalind_mrna.txt'
    finally:
        protein = open(file).read().rstrip('\n')
        print(infer_rna(protein))


if __name__ == '__main__':
    main()
