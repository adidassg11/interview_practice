# https://www.hackerrank.com/challenges/maximise-sum
#status - incomplete TODO: needs work
# start time - 10:46pm
# end time - 
# solution - 

#!/usr/bin/python

import sys

num_test_cases = int(raw_input().strip())

for t in xrange(num_test_cases):
    [a_size, mod_num] = [int(x) for x in raw_input().strip().split()]
    a = [int(x) for x in raw_input().strip().split()]

    print a_size, mod_num
    print a

    #TODO run a cleanup round after every time we add a new digit to the arrays,
    # any time we find 2 (or more) arrays that sum to the same thing, delete
    # the extras, probably just a minor optimization though...
    list_set = [[a[0]]]
    for x in a[1:]:
        print "x: %s" % x
        for t in list_set:
            print "t: %s" % t
            new_list = list(t)
            new_list.append(x)
            print 'new list: %s' % new_list
            #list_set.append(new_list)
        list_set.append([x])
        print 'full list: %s' % list_set
