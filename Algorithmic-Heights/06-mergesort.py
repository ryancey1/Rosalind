#! /usr/bin/env python3

'''

'''

import sys, os
import algorithmic_heights as algs

def main():
    # file = os.getcwd() + '/Algorithmic-Heights/rosalind_ms.txt'
    file = sys.argv[1]
    with open(file) as _:
        line = [lines.strip() for lines in _.readlines()]
        length, A = int(line[0]), [int(x) for x in line[1].split()]
    print(*algs.mergesort(A, length))

## METHODS GO HERE ##

if __name__ == '__main__':
    main()
