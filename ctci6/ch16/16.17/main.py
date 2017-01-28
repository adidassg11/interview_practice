#!/usr/bin/python

#status - COMPLETE
# start - 1038 (took a long time to think though and used 2 hints)
# end - ??? like an hour :'(
# notes: holy fuck this took so much effort, solution was to just write the cases very explicitly
#   then refactor it. Classic example of needing to have good test cases (i.e. the all negatives)

def BadArgsException(Exception):
    pass


def debug(args):
    #print(args)
    pass


# Buggy and took forever
def get_largest_sum2(a):
    if not len(a):
        raise BadArgsException

    cur_max = a[0]
    global_max = cur_max
    max_single = a[0]
    need_new_set = False

    for i in xrange(1, len(a)):
        max_single = max(max_single, a[i])

        if need_new_set:
            cur_max = a[i]

        new_total = cur_max + a[i]
        if new_total < 0:
            global_max = max(global_max, cur_max)
            need_new_set = True
            continue
        else:
            global_max = max(global_max, new_total)
            need_new_set = False

    print max(global_max, max_single)


# Buggy and took forever....
def get_largest_sum3(a):
    if not len(a):
        raise BadArgsException

    max_range = (0,0)
    max_single = a[0]
    global_max = a[0]
    local_max = a[0]
    need_new_local_max = False

    for i in xrange(1, len(a)):
        if a[i] > 0:
            local_max += a[i]
            global_max = max(global_max, local_max)
            continue

        if local_max + a[i] >= 0:
            local_max += a[i]


# Sliding window approach
def get_largest_sum_brute(a):
    debug('total array: %s' % a)
    largest_sum = a[0]

    for window_size in xrange(1, len(a)+1):
        debug('\nwindow size: %s' % window_size)
        current_sum = 0
        for starting_idx in xrange(0, len(a)-window_size+1):
            debug('starting_idx: %s' % starting_idx)
            debug('looking at: %s' % a[starting_idx:starting_idx+window_size])
            window_sum = sum(a[starting_idx : starting_idx+window_size])
            if window_sum == max(largest_sum, window_sum):
                # indexing in this print is sketchy but correct
                debug('======found new max %s in interval [%s,%s]' % (window_sum, starting_idx,
                                                                 starting_idx + window_size -1 ))
                largest_sum = window_sum

    return largest_sum


# just one pass O(n), didn't take too long :)
def get_largest_sum_on(a):
    debug('total array: %s' % a)
    largest_sum = a[0]
    current_sum = a[0]

    for i in xrange(len(a)):
        debug('a[%s]: %s' % (i, a[i]))

        if a[i] >= 0:
            # super simple case
            debug('just increasing...')
            current_sum += a[i]
            largest_sum = max(current_sum, largest_sum)
            continue

        # else a[i] is negative...
        if largest_sum < 0:
            # compare to largest single negative # seen so far,
            # current_sum (running total) is useless here...
            debug('taking largest of two negatives...')
            current_sum = 0
            largest_sum = max(a[i], largest_sum) # could rewrite...
        else:
            new_sum = a[i] + current_sum
            debug('checking if sum is negative...')
            if new_sum > 0:
                current_sum = new_sum
                largest_sum = max(current_sum, largest_sum)
            else:  
                # dipped into negative, start new sum...
                current_sum = 0

        debug('largest_sum now %s' % largest_sum)

        '''
        honestly this is so much easier when rewritten in the form of:
        if a[i] < 0 and largest_sum < 0:
            <...>
            continue
        if a[i] < 0 and largest_sum > 0:
            <...>
            continue
        <...>
        '''

    debug('====final largest sum==== %s' % largest_sum)
    return largest_sum 


# rewrite of the code above, simplified
def get_largest_sum_simple_code(a):
    debug('total array: %s' % a)
    max_sum = a[0]
    cur_sum = 0

    for i in xrange(len(a)):
        debug('looking at a[%s]: %s' % (i, a[i]))
        cur_sum += a[i]
        debug('new cursum: %s' % cur_sum)

        # order of this clause matters, putting it below the next if fails
        if cur_sum < 0:
            if max_sum < 0:
                max_sum = max(max_sum, cur_sum)
                debug('new max: %s' % max_sum)
            cur_sum = 0
        elif cur_sum > max_sum:
            max_sum = cur_sum
            debug('new max: %s' % max_sum)

    debug('==== max sum ==== %s' % max_sum)
    return max_sum


def get_largest_sum(a):
    #return get_largest_sum_brute(a)
    #return get_largest_sum_on(a)
    return get_largest_sum_simple_code(a)


assert(get_largest_sum([-5,1,0,-8]) == 1)
assert(get_largest_sum([-5,-9,0,-8]) == 0)
assert(get_largest_sum([-5,9,0,-8, 2]) == 9)
assert(get_largest_sum([-5,9,0,-8, 2, 7]) == 10)
assert(get_largest_sum([-5,9,0,-8, 11]) == 12)
assert(get_largest_sum([-5,-2,-1, -2, -5]) == -1)
## todo: add another case where max is 0
