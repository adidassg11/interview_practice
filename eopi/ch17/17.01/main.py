#!/usr/bin/python
#Status - incomplete, buggy

# Combinations
def getNumSeq1(s, w):
    ways = [0] * (s+1)
    ways[0] = 1
    '''
    i = s-1
    while i>=0:
        for x in w:
            if i-x >= 0:
                ways[i-x] = ways[i] + 1
        i -= 1
    '''
    for i in xrange(s):
        for x in w:
            if i+x <= s:
                ways[i+x] = ways[i] + 1
    print ways
    return ways[0]

# Permutations
def getNumSeq2(s, w):
    ways = [0] * (s+1)
    for x in w:
        for i in xrange(s):
            if i-x >= 0:
                ways[i] = ways[i-x] + 1

    print ways
    return ways[0]


w = [2, 3, 7] #like in football
s = 12

print getNumSeq1(s, w)
print getNumSeq2(s, w)
