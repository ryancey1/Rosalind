#! /usr/bin/env python3

import algorithmic_heights as algs
import os, sys

# 5
# 1 3 5 7 2
# 
# 7 5 1 3 2

def main():
    file = sys.argv[1]
    # file = os.getcwd() + '/Algorithmic-Heights/rosalind_hea.txt'
    with open(file) as _:
        line = [lines.strip() for lines in _]
        arr, n = [int(x) for x in line[1].split()], int(line[0])
    print(*algs.build_max_heap(arr, n))

if __name__ == '__main__':
    main()