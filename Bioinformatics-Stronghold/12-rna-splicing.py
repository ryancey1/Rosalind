#! /usr/bin/env python3

'''
'''

import sys
import re

def read_fasta(fasta_file):
    pattern = r'>.+\n([ATCG\n]+)'
    string = open(fasta_file).read()
    fasta = re.findall(pattern, string)
    for i in range(len(fasta)):
        fasta[i] = fasta[i].replace('\n', '')
    return fasta

def splice_rna(mRNA, introns):
    mature_mRNA = mRNA
    for intron in introns:
        mature_mRNA = mature_mRNA.replace(intron, '')
    return mature_mRNA

def translate(mature_mRNA):
    codon_list= {
        'TTT': 'F',      'CTT': 'L',      'ATT': 'I',      'GTT': 'V',
        'TTC': 'F',      'CTC': 'L',      'ATC': 'I',      'GTC': 'V',
        'TTA': 'L',      'CTA': 'L',      'ATA': 'I',      'GTA': 'V',
        'TTG': 'L',      'CTG': 'L',      'ATG': 'M',      'GTG': 'V',
        'TCT': 'S',      'CCT': 'P',      'ACT': 'T',      'GCT': 'A',
        'TCC': 'S',      'CCC': 'P',      'ACC': 'T',      'GCC': 'A',
        'TCA': 'S',      'CCA': 'P',      'ACA': 'T',      'GCA': 'A',
        'TCG': 'S',      'CCG': 'P',      'ACG': 'T',      'GCG': 'A',
        'TAT': 'Y',      'CAT': 'H',      'AAT': 'N',      'GAT': 'D',
        'TAC': 'Y',      'CAC': 'H',      'AAC': 'N',      'GAC': 'D',
        'TAA': 'Stop',   'CAA': 'Q',      'AAA': 'K',      'GAA': 'E',
        'TAG': 'Stop',   'CAG': 'Q',      'AAG': 'K',      'GAG': 'E',
        'TGT': 'C',      'CGT': 'R',      'AGT': 'S',      'GGT': 'G',
        'TGC': 'C',      'CGC': 'R',      'AGC': 'S',      'GGC': 'G',
        'TGA': 'Stop',   'CGA': 'R',      'AGA': 'R',      'GGA': 'G',
        'TGG': 'W',      'CGG': 'R',      'AGG': 'R',      'GGG': 'G'
    }
    start, end, protein = 0, 3, ''
    while start < len(mature_mRNA):
        codon = mature_mRNA[start:end]
        aa = codon_list.get(codon, '')
        if aa in ['Stop', 'stop']:
            break
        protein += aa
        start, end = end, end + 3
    print(protein)


if __name__ == '__main__':
    fasta_file = sys.argv[1]
    # fasta_file = '/Users/ryanyancey/Git/Rosalind/Bioinformatics-Stronghold/rosalind_splc.txt'
    seqs = read_fasta(fasta_file)
    mRNA = splice_rna(seqs[0], seqs[1:])
    translate(mRNA)

