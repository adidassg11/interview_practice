#!/usr/bin/python

#status - WIP
# start - 1038 (took a long time to think though and used 2 hints)
# end - ??? like an hour :'(

def BadArgsException(Exception):
    pass


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

get_largest_sum2([5,1,0,-8])
get_largest_sum2([-5,1,0,-8])
get_largest_sum2([-5,-9,0,-8])
get_largest_sum2([-5,9,0,-8, 2]) # broken, should be 3
get_largest_sum2([-5,9,0,-8, 11]) # broken, should be 12
