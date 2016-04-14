#!/usr/bin/python
# start 1:15am
# end
# status incomplete, stumped
# solution

import random

def randXStats(x, num_iter=1000):
    stats_dict = {}
    for i in xrange(num_iter):
        num = None
        if x == 7:
            num = rand7_2()
        else:
            num = random.randrange(x)
        if num in stats_dict:
            stats_dict[num] += 1
        else:
            stats_dict[num] = 1

    for i in xrange(x):
        print 'i:%s, percent:%s, total:%s' % (i, stats_dict.get(i, 0)/float(num_iter), stats_dict.get(i, 0))

def rand7():
    # can only use random.randrange(5)

    # adding throws things off...
    num = None
    while True:
        first_digit = random.randrange(5)
        if first_digit < 3:
            num = first_digit * 10
            break
    num += random.randrange(5)
    return num % 7

def rand7_2():
    return (random.randrange(5))*(7/5.0)%7

randXStats(7, 5000)
#print rand7()
