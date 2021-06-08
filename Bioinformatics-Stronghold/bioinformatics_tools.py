#! /usr/bin/env python3

'''
A collection of tools for processing bioinformatics data
'''

import re
from os import error

# globals
possible_nts = ['A', 'T', 'U', 'C', 'G']
comp_dna = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
comp_rna = {'A': 'U', 'U': 'A', 'C': 'G', 'G': 'C'}
transitions = {'A': 'G', 'G': 'A', 'C': 'T', 'T': 'C'}
codon_list = {'UUU': 'F', 'CUU': 'L', 'AUU': 'I', 'GUU': 'V',
              'UUC': 'F', 'CUC': 'L', 'AUC': 'I', 'GUC': 'V',
              'UUA': 'L', 'CUA': 'L', 'AUA': 'I', 'GUA': 'V',
              'UUG': 'L', 'CUG': 'L', 'AUG': 'M', 'GUG': 'V',
              'UCU': 'S', 'CCU': 'P', 'ACU': 'T', 'GCU': 'A',
              'UCC': 'S', 'CCC': 'P', 'ACC': 'T', 'GCC': 'A',
              'UCA': 'S', 'CCA': 'P', 'ACA': 'T', 'GCA': 'A',
              'UCG': 'S', 'CCG': 'P', 'ACG': 'T', 'GCG': 'A',
              'UAU': 'Y', 'CAU': 'H', 'AAU': 'N', 'GAU': 'D',
              'UAC': 'Y', 'CAC': 'H', 'AAC': 'N', 'GAC': 'D',
              'UAA': '_', 'CAA': 'Q', 'AAA': 'K', 'GAA': 'E',
              'UAG': '_', 'CAG': 'Q', 'AAG': 'K', 'GAG': 'E',
              'UGU': 'C', 'CGU': 'R', 'AGU': 'S', 'GGU': 'G',
              'UGC': 'C', 'CGC': 'R', 'AGC': 'S', 'GGC': 'G',
              'UGA': '_', 'CGA': 'R', 'AGA': 'R', 'GGA': 'G',
              'UGG': 'W', 'CGG': 'R', 'AGG': 'R', 'GGG': 'G'}

class NotInFastaError(error):
    pass


def validate_sequence(nt_sequence):
    temp, checkedUT = nt_sequence.upper(), False
    # 1. check if sequence contains U and T both (error)
    if not checkedUT:
        if 'U' in temp and 'T' in temp:
            exit("Sequence error: contains 'T' and 'U'.")
        checkedUT = True
    # 2. parse nts and validate they are
    for nt in temp:
        if nt not in possible_nts:
            return False
    return temp


def hamming_distance(seq1, seq2):
    dist = 0
    for s, t in zip(seq1, seq2):
        if s != t:
            dist += 1
    return dist


def read_fasta(filepath):
    seqDict = None
    try:
        with open(filepath) as fasta:
            if not re.search('>', open(filepath).read()):
                raise NotInFastaError
            else:
                read = [line.strip() for line in fasta]
                seqID, seqDict = '', {}

                for line in read:
                    if line.startswith('>'):
                        seqID = line
                        seqDict[seqID] = ''
                    else:
                        validated = validate_sequence(line)
                        seqDict[seqID] += validated
    except NotInFastaError:
        with open(filepath) as fasta:
            seqDict = [line.strip() for line in fasta]
    finally:
        return seqDict


def transitions_transversions(seq1, seq2):
    ts, tv = 0.0, 0.0
    for s, t in zip(seq1, seq2):
        if s != t:
            if transitions[s] == t:
                ts += 1
            else:
                tv += 1
    return ts/tv


def translate_rna_protein(seq, initial_pos = 0):
    # if not rna, transcribe it
    rna = validate_sequence(seq)
    prot = []
    if 'T' in rna:
        rna = transcribe_dna_rna(rna)
    for pos in range(initial_pos, len(rna)-2, 3):
        if codon_list[rna[pos:pos+3]] == '_':
            break
        prot += codon_list[rna[pos:pos+3]]
    # return [codon_list[rna[pos:pos+3]] for pos in range(initial_pos, len(rna)-2, 3)]
    return prot


def transcribe_dna_rna(dna):
    return dna.replace('T', 'U')


def reverse_complement(seq):
    # validate that sequence is not wrong
    if 'T' in seq and 'U' in seq:
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
    return (seq.count('G') + seq.count('C'))/len(seq)


def find_orfs(seq):
    orfs = []
    if not 'U' in seq:
        seq = transcribe_dna_rna(seq)
    for stop in ['UAA', 'UAG', 'UGA']:
        regex = f'AUG[AUCG]*{stop}'
        orfs += re.findall(r'(?=(%s))' % regex, seq)
    return orfs    
