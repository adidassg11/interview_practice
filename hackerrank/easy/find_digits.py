#!/bin/python
import sys
# https://www.hackerrank.com/challenges/find-digits

t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    n_str = str(n)
    num = 0
    import pdb; pdb.set_trace()
    for d in n_str:
        d_int = int(d)
        if d_int > 0 and divmod(n, d_int)[1] == 0:
            num += 1
    print num
