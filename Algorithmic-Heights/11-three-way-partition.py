#! /usr/bin/env python3

'''

'''

import sys, os
# import bioinformatics_tools as bfx
import algorithmic_heights as algs

## METHODS GO HERE ##
def main():
    file = None
    try:
        file = sys.argv[1]
    except (IndexError):
        file = os.getcwd() + '/Algorithmic-Heights/rosalind_par3.txt'

    with open(file) as _:
        line = [lines.strip() for lines in _.readlines()]
    
    l, arr = int(line[0]), [int(x) for x in line[1].split()]
    
    print(*algs.partition3(arr, 0, l-1))

if __name__ == '__main__':
    main()
