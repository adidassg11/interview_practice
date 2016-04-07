#!/usr/bin/python

def fact(num):
    total = num
    for x in xrange(num-1, 1, -1):
        total *= x
    return total

def getTrailingZeros(num):
    # Don't even need to do any factorializing... just get # of 5's
    return num / 5

print getTrailingZeros(4)
print fact(4)

print getTrailingZeros(7)
print fact(7)

print getTrailingZeros(20)
print fact(20)
