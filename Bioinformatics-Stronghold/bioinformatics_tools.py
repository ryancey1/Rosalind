#! /usr/bin/env python3

'''
A collection of tools for processing bioinformatics data
'''

import re

# globals
comp_dna = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
comp_rna = {'A': 'U', 'U': 'A', 'C': 'G', 'G': 'C'}
codon_list = {
    'UUU': 'F',      'CUU': 'L',      'AUU': 'I',      'GUU': 'V',
    'UUC': 'F',      'CUC': 'L',      'AUC': 'I',      'GUC': 'V',
    'UUA': 'L',      'CUA': 'L',      'AUA': 'I',      'GUA': 'V',
    'UUG': 'L',      'CUG': 'L',      'AUG': 'M',      'GUG': 'V',
    'UCU': 'S',      'CCU': 'P',      'ACU': 'T',      'GCU': 'A',
    'UCC': 'S',      'CCC': 'P',      'ACC': 'T',      'GCC': 'A',
    'UCA': 'S',      'CCA': 'P',      'ACA': 'T',      'GCA': 'A',
    'UCG': 'S',      'CCG': 'P',      'ACG': 'T',      'GCG': 'A',
    'UAU': 'Y',      'CAU': 'H',      'AAU': 'N',      'GAU': 'D',
    'UAC': 'Y',      'CAC': 'H',      'AAC': 'N',      'GAC': 'D',
    'UAA': 'Stop',   'CAA': 'Q',      'AAA': 'K',      'GAA': 'E',
    'UAG': 'Stop',   'CAG': 'Q',      'AAG': 'K',      'GAG': 'E',
    'UGU': 'C',      'CGU': 'R',      'AGU': 'S',      'GGU': 'G',
    'UGC': 'C',      'CGC': 'R',      'AGC': 'S',      'GGC': 'G',
    'UGA': 'Stop',   'CGA': 'R',      'AGA': 'R',      'GGA': 'G',
    'UGG': 'W',      'CGG': 'R',      'AGG': 'R',      'GGG': 'G'
}


def read_fasta(fasta_file):
    with open(fasta_file) as f:
        f = f.read()
        seqs = []
        matches = re.findall(r'>.*\n([ATCG\n]+)', f)
        for i in matches:
            seqs.append(i.replace('\n', ''))
        return seqs


def translate_rna_protein(rna):
    if not (len(rna) % 3 == 0):
        exit('Not a complete RNA sequence.')
    protein = ''
    # go through codons and translate into amino acids
    for position in range(0, len(rna), 3):
        start, end = position, position + 3
        codon = rna[start:end]
        aa = codon_list.get(codon, '')
        if aa in ['Stop', 'stop']:
            break
        if aa == '':
            exit(f"'{codon}' is not in codon table.")
        protein += aa
    print(protein)


def transcribe_dna_rna(dna):
    return dna.replace('T', 'U')


def reverse_complement(seq):
    # validate that sequence is not wrong
    if 'T' and 'U' in seq:
        exit('Error: Sequence cannot contain both \'T\' and \'U\' nucleotides.')
    if 'U' in seq:
        return reverse(rna_complement(seq))
    if 'T' in seq:
        return reverse(dna_complement(seq))


def reverse(seq):
    return ''.join(seq[::-1])


def dna_complement(seq):
    return [comp_dna[base] for base in seq]


def rna_complement(seq):
    return [comp_rna[base] for base in seq]


def gc_content(seq):
    seq = seq.upper()
    g, c = seq.count('G'), seq.count('C')
    return (g + c) / len(seq)
