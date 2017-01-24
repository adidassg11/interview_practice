#!/usr/bin/python

# status - COMPLETE, similar but sliiightly different from book
# start - 1130
# end - 1144 for sol #1
# end - 1215 for sol #2

# TODO: what to print if it's already sorted?

import copy

#solution 1: just make a copy, sort and compare
def find_smallest_subrange1(a):
    """
        param a is the array of ints
    """
    sorted_a = sorted(a)
    
    start_idx = 0
    end_idx = len(a)

    for i in xrange(len(a)):
        if a[i] != sorted_a[i]:
            start_idx = i
            print 'start_id: %s' % str(i)
            break

    for i in xrange(len(a)-1, -1, -1):
        if a[i] != sorted_a[i]:
            end_idx = i
            print 'end_idx: %s' % str(i)
            break

#solution 2: O(n), no extra mem
'''
    need something like an interior max and min, exterior/current high and low values (to compare to),
    and sort range (which gets updated when comparing the previous 4 vars)
'''
def find_smallest_subrange2(a):
    length = len(a)
    mid_idx = length/2

    int_max = a[mid_idx] # interior max and min
    int_min = a[mid_idx]
    start_idx = mid_idx # start and end range for the unsorted section, this is what we want to return
    end_idx = mid_idx
    cur_start_idx = mid_idx
    cur_end_idx = mid_idx

    while True:
        idx_updated = False  #### must be a better way to do this...
        if cur_start_idx > 0:
            cur_start_idx -= 1 
            idx_updated = True

        if cur_end_idx < length -1:
            cur_end_idx += 1
            idx_updated = True

        if not idx_updated:
            return (start_idx, end_idx)

        if a[cur_start_idx] > int_min:
            start_idx = cur_start_idx
            print 'found smaller going left, idx %s and value is %s' % (start_idx, a[cur_start_idx])

        if a[cur_end_idx] < int_max:
            end_idx = cur_end_idx
            print 'found larger going right, idx %s and value is %s' % (end_idx, a[cur_end_idx])

        int_max = max(a[cur_start_idx], int_max)
        int_min = min(a[cur_end_idx], int_min)


#             3     5     7   8   9 
s = [1, 2, 4, 6, 7, 7, 7, 10, 11, 12, 16, 18, 19] ### SORTED a
a = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]

#find_smallest_subrange1(a)
print find_smallest_subrange2(a)
#find_smallest_subrange1([0])
#find_smallest_subrange1([-1, 1])
#find_smallest_subrange1([1, -1, 1])
print find_smallest_subrange2([1, -1, 1])
