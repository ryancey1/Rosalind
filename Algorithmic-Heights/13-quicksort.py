#! /usr/bin/env python3

'''

'''

import sys, os
# import bioinformatics_tools as bfx
import algorithmic_heights as algs

## METHODS GO HERE ##
def main():
    try:
        file = sys.argv[1]
    except (IndexError):
        file = os.getcwd() + '/Algorithmic-Heights/rosalind_qs.txt'
    finally:
        with open(file) as _:
            line = [lines.strip() for lines in _.readlines()]
        length, arr = int(line[0]), [int(x) for x in line[1].split()]
        length, arr = 7, [int(x) for x in '5 -2 4 7 8 -10 11'.split()]
        print(*algs.quicksort(arr, 0, length-1))
        
if __name__ == '__main__':
    main()
