#! /usr/bin/env python3

'''

'''

import sys, os
import algorithmic_heights as algs

# def binary_search(value, array, start, end):
#     assert sorted(array) == array # confirm the array is sorted
#     l, r = start, end
#     m = (l + (r - l) // 2) 
#     if value == array[m]:
#         return m + 1
#     if l > r:
#         return -1
#     elif array[m] > value:
#         return binary_search(value, array, l, m-1)
#     else:
#         return binary_search(value, array, m+1, r)
    
def main():
    # file = os.getcwd() + '/Algorithmic-Heights/rosalind_bins.txt'
    file = sys.argv[1]
    with open(file) as input:
        f = [x.strip() for x in input.readlines()]
        n, m, A, L = int(f[0]), int(f[1]), [int(x) for x in f[2].split()], [int(x) for x in f[3].split()]
    
    answer = []
    for i in range(m):
        answer.append(algs.binary_search(L[i], A, 0, n-1))
    print(*answer)

if __name__ == '__main__':
    main()