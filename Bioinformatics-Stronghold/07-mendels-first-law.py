#! /usr/bin/env python3

'''
Calculating Mendel's First Law Problem

Given: Three positive integers k, m, and n, representing a population containing k+m+n organisms: k individuals are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.

Return: The probability that two randomly selected mating organisms will produce an individual possessing a dominant allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate.
'''
import sys

## IMPORTANT: there are fewer ways to have two recessive alleles, so we will calculate 
## the probability that occurs and subtract it from 1 to obtain the correct answer

##  two recessive (4/4)       two heterozygous (1/4)        heterozygous x recessive (2/4)      homozygous x recessive (0/4)    homozygous x heterozygous (0/4)
##      x   x                          X   x                    X   x                                   X   X                       X   X
##  x   xx  xx                     X   XX  Xx               x   Xx  xx                              x   Xx  Xx                  X   XX  XX
##  x   xx  xx                     x   Xx  xx               x   Xx  xx                              x   Xx  Xx                  x   Xx  Xx



# step1, calculate the total
vals = open(sys.argv[1]).read().rstrip('\n').split()
k,m,n = float(vals[0]), float(vals[1]), float(vals[2])
total = k + m + n

# step2, calculate the probability of two recessive parents mating and producing homozygous recessive
r_r = (n/total) * ((n-1)/(total-1)) * (4/4)

# step3, calculate the probability of two heterozygous parents mating and producing a homozygous recessive
h_h = (m/total) * ((m-1)/(total-1)) * (1/4)

# step4, calculate the probability of heterozygous x recessive parents mating and producing a homozygous recessive
h_r = ((m/total) * (n/(total-1)) + (n/total) * (m/(total-1))) * (2/4)

# step5 
recessive_total = r_r + h_h + h_r
dominant_total = 1 - recessive_total
print(dominant_total)