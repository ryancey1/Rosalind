#! /usr/bin/env python3

import sys, os
import algorithmic_heights as algs

def main():
    file = sys.argv[1]
    # file = os.getcwd() + '/Algorithmic-Heights/rosalind_ins.txt'
    with open(file) as f:
        line = [lines.strip() for lines in f.readlines()]
        n, arr = int(line[0]), [int(x) for x in line[1].split()]
    
    print(algs.insertion_sort(arr, n))
    
if __name__ == '__main__':
    main()