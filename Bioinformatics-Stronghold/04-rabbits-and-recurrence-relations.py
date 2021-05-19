#! /usr/bin/env python3

'''
Given: Positive integers n≤40 and k≤5.
Return: The total number of rabbit pairs that will be present after n months, if we begin with 1 pair and in each generation, every pair of reproduction-age rabbits produces a litter of k rabbit pairs (instead of only 1 pair).
'''

n = 5
k = 3

def fib(n, k):
    if n == 0:
        return 1
    elif n == 1:
        return k
    else:
        return fib(n-1, k) + fib(n-2, k)

print(fib(n, k))