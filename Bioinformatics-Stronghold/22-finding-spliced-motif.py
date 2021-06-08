#! /usr/bin/env python3

'''

'''

import sys, time
import bioinformatics_tools as bfx

# def spliced_motif(dna, motif):
#     index, pos, place = [], 0, 0
#     for nt in motif:
#         for i in range(place, len(dna)):
#             if dna[i] == nt:
#                 if pos > 0 and i+1 > index[pos-1]:
#                     index.append(i + 1)
#                     place = i+1
#                     pos+=1
#                 elif pos == 0:
#                     index.append(i + 1)
#                     place = i+1
#                     pos+=1
#         pos = place
#     return index

def spliced_motif(dna, motif):
    offset = 1
    indices, answer = [], []

    for i in range(len(motif)):
        indices.append([])
        j = 0
        while j <= len(dna):
            if motif[i] == dna[j]:
                indices[i].append(j + offset)
            j += 1

    for i in range(len(indices)):
        for x in range(len(indices[i])):
            if len(answer) == 0:
                answer.append(indices[i][x])
                break
            elif answer[i-1] < indices[i][x]:
                answer.append(indices[i][x])
                break
    
    print(*answer, sep = " ")

if __name__ == '__main__':
    dna = 'GGTCTGACGTTTTTCCCCCCTAGTGTTCTGGGGTCAGTAATGTATGGTCAATTCGTAGGTGTTTACATACTTTTTTTGTTATGAGCCCATTGGCGCACCGAGCACAGTTCTGCTAACTGGATTGAAGATATGTCGAGGACATCCATGGATCGGCCTTAGCGTTTGGAGCTGGTCTTGGGATCTCGTAGAGATGAACTTACTCAACTCTATATATTGCATCTTTAAACGTGGCAACGAACCGGCCGCAGAATACAATGTTGCCCTACCCTTATGTGGACTGATGGCCCTGGTAGTTCTCCTTGGTACACTTGCCACAGGGGTTATAGGTTAGTGTTCTTGAGGTAGTTGGAGTTGAAATCTAGGTCGGTTAAAGTGCCCATCCCCTTGGATGAAATGTCAGCCTTGGATAACGCCGCGCCGTACCGACCCCCTAAGGCGGTGGCGACTCGGGGAAGCCAGTGGCTTTAGACAGCTGCGCCCGCAGCGCGCCTGCCGCTTAGATCGCTGCTGAATATTCCGCTCTTTTTTCTTCCATCCCACTACACCATGAGTGTACAGAGCATTCGCACTCGTCAACGACTAACCATGTGCATAATTTTGCTTGGCATTTACAAGCAGGGCAGACAAATCCATTCATCCTATCTTGGGCATAGCGTGGGCGACTAAAAGCGAAAGACGCTCGCATGGTTTGTTCTTCTTCGCCGATACTGCGTTGCGCCGAATTAAAGGCCTTAAAATGGTCCGGATAGTCGGGCTTGTAGCCGAAGACCCTCTCCCCTAATAATGTTGGAGCTCGCAAAATTAGAATAGTCGTAGCGAGTCGGCACGTCGTGCTTATGGGCGCATAACTGTAATTGGGAACCGAATAATCACTTCGAGTTGGGAATGGTAGTTCATCTAATCATTTATGGATTCTGAGAGACTACACCCTATTAAAACGTATACCCTTCGTGCTAGCTCCCCCGTTGAGATTTCCGACAC'
    motif = 'TGTCTTACGTACTTTTACAATTAGGCCAGATTTTAAT'

    start = time.perf_counter()
    spliced_motif(dna, motif)
    print(round(time.perf_counter() - start, 6))