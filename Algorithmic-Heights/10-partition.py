#! /usr/bin/env python3

'''

'''

import sys, os, random
# import bioinformatics_tools as bfx
import algorithmic_heights as algs

# def partition(arr, pivot, end):
#     # 1. move pivot to the end of the array
#     # 2. find first item from RIGHT < pivot
#     # 3. find first item from LEFT > pivot
#     # 4. swap right and left
#     arr = swap(arr, pivot, end)
#     pivot = end
#     fromL, fromR = 0, pivot-1
#     while True:
#         for i in range(fromR, -1, -1):
#             if arr[i] < arr[pivot]:
#                 fromR = i; break
#         for i in range(fromL):
#             if arr[i] > arr[pivot]:
#                 fromL = i; break
#         if fromR < fromL:
#             break
#         arr = swap(arr, fromL, fromR)
#         fromL, fromR = fromR, fromL
#     arr = swap(arr, pivot, fromL)
#     return arr
        
# def swap(arr, item1, item2):
#     arr[item1], arr[item2] = arr[item2], arr[item1]
#     return arr

## METHODS GO HERE ##
def randomArrayGenerator(n = 10, bound = 100):
    arr = [random.randint((-1*bound), bound) for _ in range(n)]
    return arr


def main():
    file = None
    try:
        file = sys.argv[1]
    except (IndexError):
        file = os.getcwd() + '/Algorithmic-Heights/rosalind_par3.txt'
    
    with open(file) as _:
        line = [lines.strip() for lines in _]
        length, arr = int(line[0]), [int(x) for x in line[1].split()]
   
    if len(arr) != length:
        exit("Something is wrong with the input.")
    
    # print(*arr)
    print(*algs.partition(arr, 0, length-1))


if __name__ == '__main__':
    main()
