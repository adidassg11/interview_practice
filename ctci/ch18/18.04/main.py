#!/usr/bin/python
# start time - 1:33
# end time - 
# status - incomplete, take another look in the future
# solution - 

def numTwosSingleNum(num):
    total_twos = 0
    while num > 0:
        new_digit = num % 10
        if new_digit == 2:
            total_twos += 1
        num /= 10
    return total_twos


def numTwosTotal(target):
    return numTwosTotalBrute(target)

def numTwosTotalBrute(target):
    total_twos = 0
    if target < 2:
        return 0

    for i in xrange(2, target+1):
        total_twos += numTwosSingleNum(i)
    print 'numTwosTotalBrute(%s): %s' % (str(target), total_twos)


numTwosTotalBrute(2)
numTwosTotalBrute(11)
numTwosTotalBrute(12)
numTwosTotalBrute(20)
numTwosTotalBrute(22)
