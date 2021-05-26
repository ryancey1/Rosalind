#! /usr/bin/env python3

'''

'''

import re
import sys
import bioinformatics_tools as bfx

start_codons, stop_codons = ['ATG'], ['TAA', 'TAG', 'TGA']
orfs = []
proteins = []

def revcom(dna):
    complement = dna.lower()
    complement = complement.replace('a', 'T')
    complement = complement.replace('t', 'A')
    complement = complement.replace('c', 'G')
    complement = complement.replace('g', 'C')
    return complement[::-1]    

def translate(orf):
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
    while start < len(orf):
        codon = orf[start:end]
        aa = codon_list.get(codon, '')
        if aa in ['Stop', 'stop']:
            break
        protein += aa
        start, end = end, end + 3
    if protein not in proteins:
        proteins.append(protein)

def find_orfs(dna):
    orfs = []
    start, end = 0, 3
    length = len(dna)

    while start < length:
        this_codon = dna[start:end]
        if this_codon not in start_codons:
            start, end = start+1, end+1
        else:
            orf_start, orf_end = start, end
            while dna[orf_start:orf_end] not in stop_codons:
                orf_start, orf_end = orf_end, orf_end+3
                last_codon = dna[orf_start:orf_end]
                if orf_end > length:
                    break
            if last_codon in stop_codons:
                orfs.append(dna[start:orf_end])
            start, end = start+1, end+1
        
def regex_find_orfs(dna):
    for start_codon in re.finditer(r'ATG', dna):
        start, end = start_codon.start(), start_codon.end()
        orf = dna[start:end]
        while dna[end-3:end] not in stop_codons:
            end += 3
            if end > len(dna):
                break
        if dna[end-3:end] in stop_codons and dna[start:end] not in orfs:
            orfs.append(dna[start:end])

def read_fasta(dna):
    fasta = re.search(r'>.*\n([ATCG\n]+)', dna).group(1)
    fasta = fasta.replace('\n', '')
    return fasta


if __name__=='__main__':
    file = '/Users/ryanyancey/Git/Rosalind/Bioinformatics-Stronghold/rosalind_orf.txt'
    dna = open(file).read().rstrip('\n')
    dna = read_fasta(dna)
    if len(dna) > 1000:
        sys.exit('Imported DNA is longer than 1kbp.')
    regex_find_orfs(dna)
    regex_find_orfs(bfx.reverse_complement(dna))
    for orf in orfs:
        translate(orf)
    for protein in proteins:
        print(protein)