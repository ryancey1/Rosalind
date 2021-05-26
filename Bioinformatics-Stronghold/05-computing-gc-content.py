#! /usr/bin/env python3

'''

'''
import sys
import re
import bioinformatics_tools as bfx

def count_gc(dna):
    dna = dna.replace('\n', '')
    g, c = dna.count('G'), dna.count('C')
    gc = g + c
    gc_pct = (gc/len(dna)) * 100
    return gc_pct

def find_max(dictionary):
    K, V = None, -1
    for k, v in dictionary.items():
        if v > V:
            V = v
            K = k
    return [ K , V ]

if __name__ == '__main__':
    dna = open('/Users/ryanyancey/Git/Rosalind/Bioinformatics-Stronghold/rosalind_gc.txt').read()
    gc_dict = {}
    seqs = re.findall(r'>(.*)\n([ATCG\n]+)', dna)

    for sequence in seqs:
        gc_dict[sequence[0]] = count_gc(sequence[1])

    # get key of maximum gc string
    result = find_max(gc_dict)

    # print max
    print(f'{result[0]}\n{result[1]}')