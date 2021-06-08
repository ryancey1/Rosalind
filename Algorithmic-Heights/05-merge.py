#! /usr/bin/env python3

'''

'''

import sys, os
import algorithmic_heights as algs

## METHODS GO HERE ##
def main():
    # file = sys.argv[1]
    file = os.getcwd() + '/Algorithmic-Heights/rosalind_mer.txt'
    with open(file) as _:
        line = [lines.strip() for lines in _]
        n, A, m, B = int(line[0]), [int(i) for i in line[1].split()], int(line[2]), [int(j) for j in line[3].split()]

    print(*algs.merge(A, B, n, m))

if __name__ == '__main__':
    main()
