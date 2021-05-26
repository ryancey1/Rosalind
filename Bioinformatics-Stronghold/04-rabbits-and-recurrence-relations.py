#! /usr/bin/env python3

'''
Given: Positive integers n≤40 and k≤5.

Return: The total number of rabbit pairs that will be present after n months, if we begin with 1 pair and in each generation, every pair of reproduction-age rabbits produces a litter of k rabbit pairs (instead of only 1 pair).
'''

import sys

def fib_memo(month, litter_size, memo):
    args = (month, litter_size)
    if args in memo:
        return memo[args]
    if month == 1:
        return 1
    if month == 2:
        return 1
    else:
        gen1 = fib_memo(month - 1, litter_size, memo)
        gen2 = (fib_memo(month - 2, litter_size, memo) * litter_size)
        memo[args] = gen1 + gen2
        return gen1 + gen2

if __name__ == '__main__':
    # if a file is given
    file = open(sys.argv[1]).read()
    nk = file.split()
    n, k = int(nk[0]), int(nk[1])
    if n > 40 or k > 5:
        exit('Either the number of months or offspring number is too large.')
    # process the input and print the result
    print(fib_memo(n, k, {}))