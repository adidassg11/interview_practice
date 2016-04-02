# https://www.hackerrank.com/challenges/missing-numbers
# status - complete
# start time - 9:40pm
# end time -  10:38pm, tried several methods
# solution - O(m+n) with O(100) (constant) memory, could do it slightly better with array instead of dict....

#!/usr/bin/python

import sys

a_size = int(raw_input().strip())
a = [int(x) for x in raw_input().strip().split()]
b_size = int(raw_input().strip())
b = [int(x) for x in raw_input().strip().split()]

'''
# this is aloga + blogb + O(a+b) with small mem footprint
a = sorted(a)
b = sorted(b)
i = 0
j = 0
missing_from_b = set()
last_i = a[0]
last_j = b[0]
while i<a_size-1 and j<b_size-1:
    if a[i] == b[i]:
        i += 1
        j += 1
    elif a[i] < b[j]:
        missing_from_b.add(a[i])
        i += 1
    else: #a[i] > b[j]:
        missing_from_b.add(b[i])
        j += 1

# search the rest of b
for extra_num in b[j+1:]:
    missing_from_b.add(extra_num)
'''

#this is O(a+b) == O(2b) == O(b) with small mem footprint, slightly better depending on size of a (up to 2x)
# pretend this is a bitmap...
# TODO: not working yet
'''
nums_in_b = []
missing_from_b = set()
for i in xrange(201):
    nums_in_b.append('x') # create a list of non integers...

first_b = b[0] # value around which we'll insert into array, everything relative to this
nums_in_b[99] = first_b
for x in b[1:]:
    index = x - first_b + 100
    if nums_in_b[index] == 'x':
        nums_in_b[index] = 1
    else:
        nums_in_b[index] += 1

b_array_str = ''
for i in xrange(len(nums_in_b)):
    b_array_str += '%s:%s ' % (str(i), str(nums_in_b[i]))
print b_array_str

for x in a:
    index = 
    #TODO: decrement the numbers then find the values greater than 0, this saves a little memory over the dict solution

'''
nums_in_b = {}
for x in b:
    if x in nums_in_b:
        nums_in_b[x] += 1
    else:
        nums_in_b[x] = 1
#print nums_in_b

for x in a:
    nums_in_b[x] -= 1

print ' '.join([str(x) for x in nums_in_b if nums_in_b[x] != 0])
