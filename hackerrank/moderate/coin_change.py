# https://www.hackerrank.com/challenges/coin-change
# status - incomplete WTF need to figure out simple bug
# start time - 11:14pm
# end time - 11:57

#!/usr/bin/python

# Input
# n: amount to make change for
# m: # of types of available coins (ie nickel, dime, etc)
# c: values of coins available
[n, m] = [int(x) for x in raw_input().strip().split()]
c = [int(x) for x in raw_input().strip().split()]

# Output:
# One integer which is the number of ways in which we can get a sum of N from the given infinite supply of M types of coins

coin_map = [0]*(n+1)
coin_map[0] = 1
for x in xrange(n+1):
    for coin_val in c:
        if x + coin_val < (n+1):
            #print 'adding x %s and coin %s' % (x, coin_val)
            if x == 0:
                coin_map[x+coin_val] = 1
            else:
                coin_map[x+coin_val] = coin_map[x] + 1
            #coin_map[x+coin_val] += 1

#print coin_map
print coin_map[n]
'''
t, n = map(int, raw_input().split())
nums = map(int, raw_input().split())
dp = [0]*(t+1)
dp[0] = 1
for i in xrange(1, n+1):
    for j in xrange(1, t+1):
        if j >= nums[i-1]:
            dp[j] += dp[j-nums[i-1]]
print dp[-1]
'''

