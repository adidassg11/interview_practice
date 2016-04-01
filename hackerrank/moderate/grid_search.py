# https://www.hackerrank.com/challenges/the-grid-search
# status - complete

#!/bin/python

import sys


t = int(raw_input().strip())
outputs = []
for a0 in xrange(t):
    R,C = raw_input().strip().split(' ')
    R,C = [int(R),int(C)]
    #import pdb; pdb.set_trace()
    G = []
    G_i = 0
    for G_i in xrange(R):
       G_t = str(raw_input().strip())
       G.append(G_t)
    r,c = raw_input().strip().split(' ')
    r,c = [int(r),int(c)]
    P = []
    P_i = 0
    for P_i in xrange(r):
       P_t = str(raw_input().strip())
       P.append(P_t)

    grid_match_found = False
    for i in xrange(R-r+1):
        #print G[i][:C-c+1]
        for j in xrange(C-c+1):
            if G[i][j] == P[0][0]:
                # Potential match, check grids
                mismatch_found = False
                for y in xrange(r):
                    for x in xrange(c):
                        if G[i+y][j+x] != P[y][x]:
                            mismatch_found = True
                            break
                    if mismatch_found:
                        break
                if not mismatch_found:
                    grid_match_found = True
                    #print "YES"
                    outputs.append("YES")
                    #confusing, but print in terms of x,y (col, row)
                    #print "G(%s,%s):%s" % (j, i, G[i][j])

    if not grid_match_found:
        #print "NO"
        outputs.append("NO")

for o in outputs:
    print o
