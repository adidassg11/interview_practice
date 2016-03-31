#!/bin/python
import sys

# Practicing for https://www.hackerrank.com/challenges/manasa-and-stones

num_tests = int(raw_input())

for i in xrange(num_tests):
    num_stones = int(raw_input())
    a = int(raw_input())
    b = int(raw_input())
    results = {0, 0}
    for i2 in xrange(num_stones-1):
        prev_results = results.copy()
        results.clear()
        for r in prev_results:
            results.add(r+a)
            results.add(r+b)

    print ''.join(str(x) for x in sorted(results))

