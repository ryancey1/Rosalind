#! /usr/bin/env python3

'''
Given: A positive integer n≤25.

Return: The value of F(n).
'''

import sys
import algorithmic_heights as algs

## METHODS GO HERE ##

# def fibonacci_memoized(n, memo = {0:0, 1:1}):
#     if n in memo:
#         return memo[n]
#     else:
#         memo[n-1], memo[n-2] = fibonacci_memoized(n-1, memo), fibonacci_memoized(n-2, memo)
#         return memo[n-1] + memo[n-2]

# def fibonacci_recursive(n):
#     if n == 1:
#         return 1
#     if n == 0:
#         return 0
#     else:
#         return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

def main():
    n = int(open(sys.argv[1]).read().strip())
    print(algs.fibonacci_memoized(n))

if __name__ == '__main__':
    main()