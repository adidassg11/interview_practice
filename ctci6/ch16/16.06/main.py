#!/us/bin/python

# status - complete, correct
# time started - 9:30
# time ended - 9:50
# solution - O(mlogm + nlogn + m + n), sort each list then walk thru them

import sys

# O(n^2) brute force method
def diff_brute(a1, a2):
    smallest_diff = sys.maxint

    for x in a1:
        for y in a2:
            diff = x - y
            if diff > 0 and diff < smallest_diff:
                #print 'new diff found: %s - %s = %s' % (x, y, diff)
                smallest_diff = diff

    return smallest_diff

# O(mlogm + nlogn + m + n)
def diff_better(a1, a2):
    smallest_diff = sys.maxint

    # first sort our lists
    a1 = sorted(a1)
    a2 = sorted(a2)

    
    i, j = 0, 0
    while i < len(a1) and j < len(a2):
        diff = a1[i] - a2[j]
        if diff < 0:
            i += 1
            continue
        else:
            smallest_diff = min(diff, smallest_diff)
            j += 1 # incrementing j will give us a chance at an even smaller difference
            
    return smallest_diff

'''
sorted: 1 2 3 11 15
        8 23 19 127 235
'''

#diff_brute([1,3,15,11,2], [23,127,235,19,8])
print diff_better([1,3,15,11,2], [23,127,235,19,8])
            
