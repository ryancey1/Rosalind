#! /usr/bin/env python3

'''

'''
import sys
import re
import bioinformatics_tools as bfx

# def count_gc(dna):
#     dna = dna.replace('\n', '')
#     g, c = dna.count('G'), dna.count('C')
#     gc = g + c
#     gc_pct = (gc/len(dna)) * 100
#     return gc_pct

# def find_max(dictionary):
#     K, V = None, -1
#     for k, v in dictionary.items():
#         if v > V:
#             V = v
#             K = k
#     return [ K , V ]

# if __name__ == '__main__':
#     dna = open('/Users/ryanyancey/Git/Rosalind/Bioinformatics-Stronghold/rosalind_gc.txt').read()
#     gc_dict = {}
#     seqs = re.findall(r'>(.*)\n([ATCG\n]+)', dna)

#     for sequence in seqs:
#         gc_dict[sequence[0]] = count_gc(sequence[1])

#     # get key of maximum gc string
#     result = find_max(gc_dict)

#     # print max
#     print(f'{result[0]}\n{result[1]}')

'''
1. read data from fasta file
2. clean data read into usable format
3. calculate gc content of all sequences
4. return the id/value of the highest %gc dna
'''

# returns the Rosalind format for dict entry with max GC percent
def get_max_gc(gc_dict):
    maxID, maxGC = '', 0.0
    for currID, currGC in gc_dict.items():
        if currGC > maxGC:
            maxID, maxGC = currID, currGC
    return f'{maxID.lstrip(">")}\n{maxGC}'

if __name__ == '__main__':
    filepath = 'rosalind_gc.txt'
    dna_file = bfx.read_fasta(filepath)

    # initiate gc dict
    gc = {}

        

    result = get_max_gc(gc)
    print(result)
    