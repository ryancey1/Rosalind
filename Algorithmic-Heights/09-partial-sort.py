#! /usr/bin/env python3

'''

'''

import sys, os
import algorithmic_heights as algs

## METHODS GO HERE ##
def main():
    # file = sys.argv[1]
    file = os.getcwd() + '/Algorithmic-Heights/rosalind_ps.txt'    
    with open(file) as _:
        line = [lines.strip() for lines in _]
        l, arr, num = int(line[0]), [int(x) for x in line[1].split()], int(line[2])
        # print(*algs.mergesort(arr, l)[:num]) # definitely faster
        print(*algs.heapsort(arr, l)[:num]) # way slower ???
        
        
if __name__ == '__main__':
    main()
