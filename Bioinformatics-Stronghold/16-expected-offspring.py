#! /usr/bin/env python3

'''
'''
import sys

file = sys.argv[1]
# file = '/Users/ryanyancey/Git/Rosalind/Bioinformatics-Stronghold/rosalind_iev.txt'
args = open(file).read().rstrip('\n')
args = args.split()

AA_AA = int(args[0]) # 2 * Pr(A[Aa]) = 2*1.0
AA_Aa = int(args[1]) # 2 * Pr(A[Aa]) = 2*1.0
AA_aa = int(args[2]) # 2 * Pr(A[Aa]) = 2*1.0
Aa_Aa = int(args[3]) # 2 * Pr(A[Aa]) = 2*0.75
Aa_aa = int(args[4]) # 2 * Pr(A[Aa]) = 2*0.5
aa_aa = int(args[5]) # 2 * Pr(A[Aa]) = 2*0.0

expected_offspring = (AA_AA * 2 * 4/4) + (AA_Aa * 2 * 4/4) + (AA_aa * 2 * 4/4) + (Aa_Aa * 2 * 3/4) + (Aa_aa * 2 * 2/4) + (aa_aa * 2 * 0/4)

print(expected_offspring)
