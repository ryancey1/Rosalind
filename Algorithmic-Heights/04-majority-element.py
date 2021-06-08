#! /usr/bin/env python3

'''
4 8
5 5 5 5 5 5 5 5
8 7 7 7 1 7 3 7
7 1 6 5 10 100 1000 1
5 1 6 7 1 1 10 1
'''

import sys, os
import algorithmic_heights as algs

## METHODS GO HERE ##
def main():
    file = sys.argv[1]
    # file = os.getcwd() + '/Algorithmic-Heights/rosalind_maj.txt'
    with open(file) as input:
        line = [lines.strip() for lines in input]
        _, n = [int(x) for x in line[0].split()]
        arrs = [lst.split() for lst in line[1:]]
        # for ix, lst in enumerate(arrs):
        #     arrs[ix] = [int(x) for x in lst]
    counter = [algs.majority_element(arr, n) for arr in arrs]
    print(*counter)

if __name__ == '__main__':
    main()