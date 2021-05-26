#! /usr/bin/env python3

'''
'''
import sys
import re
import bioinformatics_tools as bfx

restriction_sites = []
lengths = list(range(4,13,1))

def find_palindromes(dna):
    len_dna, len_lengths = len(dna), len(lengths)
    for start in range(len_dna):
        for i in range(len_lengths):
            length = lengths[i]
            end = start + length
            if end > len_dna:
                break
            segment, rx = dna[start:end], bfx.reverse_complement(dna[start:end])
            if segment == rx:
                restriction_sites.append(f'{start+1} {len(segment)}')

# def read_fasta(fasta):
#     seqs = re.findall(r'>.+\n([ATCG\n]+)', fasta)
#     return seqs

def main(seqs):
    for dna in seqs:
        dna = dna.replace('\n', '')
        find_palindromes(dna)
    for rx in restriction_sites:
        print(rx)

if __name__ == '__main__':
    file = sys.argv[1]
    # file = '/Users/ryanyancey/Git/Rosalind/Bioinformatics-Stronghold/rosalind_revp.txt'
    seqs = bfx.read_fasta(file)
    # seqs = ['TTTAAATTTAAA']
    main(seqs)



