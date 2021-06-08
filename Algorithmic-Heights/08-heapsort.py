#! /usr/bin/env python3

'''

'''

import sys, os
import algorithmic_heights as algs

## METHODS GO HERE ##
def main():
    file = sys.argv[1]
    
    with open(file) as _:
        line = [lines.strip() for lines in _]
        arr, n = [int(x) for x in line[1].split()], int(line[0])
    
    print(*algs.heapsort(arr, n))


if __name__ == '__main__':
    main()
