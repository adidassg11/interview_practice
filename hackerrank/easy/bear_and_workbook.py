#!/bin/python
import sys

# from https://www.hackerrank.com/challenges/bear-and-workbook

#n,k = raw_input().strip().split()
(num_chapters, prop_per_ch) = (int(x) for x in raw_input().strip().split())
t = [int(t) for t in raw_input().strip().split()]

print num_chapters, prop_per_ch, t

page_num = 0
special_problems = 0
for n in xrange(1, num_chapters+1):
    for p in xrange(1, t[n-1]+1):
        if divmod(p, prop_per_ch)[1] == 1:
            page_num += 1
        if p == page_num:
            print 'chapter %s page%s' %(n, p)
            special_problems += 1
            
print special_problems
