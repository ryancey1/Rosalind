#! /usr/bin/env python3

'''

'''

import sys
import bioinformatics_tools as bfx

def longest_common_sequence(seq1, seq2):
    em, en = len(seq1), len(seq2)
    lcs_table = [[0 for m in range(en)] for n in range(em)]
    
    for i in range(1, len(seq1)):
        for j in range(1, len(seq2)):
            if seq1[i-1] == seq2[j-1]:
                lcs_table[i][j] = 1 + lcs_table[i-1][j-1]
            else:
                lcs_table[i][j] = max(lcs_table[i][j-1], lcs_table[i-1][j])
    return lcs_table

def backtrack(lcs_table, seq1, seq2, m, n):
    lcs = ''
    while m > 0 and n > 0:
        if seq1[m-1] == seq2[n-1]:
            lcs = seq1[m-1] + lcs
            m, n = m-1, n-1
        elif lcs_table[m-1][n] > lcs_table[m][n-1]:
            m -= 1
        else:
            n -= 1
    return lcs

if __name__ == '__main__':
    file = '/Users/ryanyancey/Git/Rosalind/Bioinformatics-Stronghold/rosalind_lcsq.txt'
    # file = sys.argv[1]
    seqs = bfx.read_fasta(file)
    seq1, seq2 = seqs.values()
    table = longest_common_sequence(seq1, seq2)
    lcs = backtrack(table, seq1, seq2, len(seq1)-1, len(seq2)-1)
    print(lcs)