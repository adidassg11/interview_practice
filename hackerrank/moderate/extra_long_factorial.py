#!/bin/python
# https://www.hackerrank.com/challenges/extra-long-factorials
import sys


n = int(raw_input().strip())

factorials = [1, 1]

for i in xrange(2, n+1):
    next_num = factorials[i-1]*i
    factorials.append(next_num)
    #print i, next_num

print factorials[n]
