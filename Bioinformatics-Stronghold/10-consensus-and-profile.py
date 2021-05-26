#! /usr/bin/env python3

''' '''

import sys, re

def read_fasta(file):
    # extract all sequences in the file
    seqs = re.findall(r'>.*\n([ATCG\n]+)', file.read())
    # remove all newline characters from sequences
    for i in range(len(seqs)):
        seqs[i] = seqs[i].replace('\n', '')
    # return result
    return seqs

def profile(sequences):
    profile = []
    consensus = ''
    for i in range(len(sequences[0])):
        counter = {}
        for seq in sequences:
            for base in ['A', 'C', 'G', 'T']:
                if seq[i] == base:
                    counter[base] = counter.get(base, 0) + 1
        profile.append(counter)
        consensus += max(counter, key = counter.get)
    print(consensus)

    for base in ['A', 'C', 'G', 'T']:
        s = f'{base}: '
        for nt in profile:
            prof = nt.get(base, 0)
            s += f'{prof} '
        print(s)

if __name__ == '__main__':
    file = open(sys.argv[1])
    seqs = read_fasta(file)
    prof = profile(seqs)