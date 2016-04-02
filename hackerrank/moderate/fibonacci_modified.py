# https://www.hackerrank.com/challenges/fibonacci-modified
# status - complete
# start time - 1:02 pm
# end time - 1:18 pm

#!/usr/bin/python

def fibm(a, b, n):
    tn = a
    tn1 = b
    for i in xrange(2, n):
        tn2 = pow(tn1, 2) + tn
        #print 'tn:%s tn1:%s tn2:%s i:%s' % (tn, tn1, tn2, i)
        tn = tn1
        tn1 = tn2
    
    return tn2


[a, b, n] = [int(x) for x in raw_input().strip().split()]

print fibm(a, b, n)
