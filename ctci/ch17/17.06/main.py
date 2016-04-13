#!/usr/bin/python
#start time - 4:17pm
#end time:
# status complete?
# solution - O(n) time and O(1) mem

# trivial solution, O(nlogn)
# compare with sorted array
def get_index_range(a):
    start_index = 0
    end_index = len(a) - 1
    sorted_array = sorted(a)
    for i in xrange(len(a)):
        if a[i] != sorted_array[i]:
            start_index = i
            break
    for i in xrange(len(a)-1, 0, -1):
        if a[i] != sorted_array[i]:
            end_index = i
            break

    print start_index, end_index 

# use O(n) time to walk through
def get_index_range2(a):
    start_index = 0
    end_index = len(a) - 1
    beg_of_middle_arr = 0
    end_of_middle_arr = len(a)-1

    # Find middle array that for sure needs to be sorted
    for i in xrange(1, len(a)-1):
        if a[i] < a[beg_of_middle_arr]:
            beg_of_middle_arr = i
            break
        else:
            beg_of_middle_arr = i
            
    for i in xrange(len(a)-2, 0, -1):
        if a[i] > a[end_of_middle_arr]:
            end_of_middle_arr = i
            break
        else:
            end_of_middle_arr = i
    
    print ['%s:%s'%(x,str(a[x])) for x in xrange(len(a))]
    print beg_of_middle_arr, end_of_middle_arr

    # Get min and max of middle array
    min_index = beg_of_middle_arr
    max_index = beg_of_middle_arr

    for i in xrange(beg_of_middle_arr, end_of_middle_arr+1):
        if a[i] < a[min_index]:
            min_index = i
        if a[i] > a[max_index]:
            max_index = i

    print 'min max %s %s' % (min_index, max_index)

    # now expand the middle array left
    new_beg_of_middle = beg_of_middle_arr
    for i in xrange(beg_of_middle_arr - 1, -1, -1):
        if a[i] > a[min_index]:
            new_beg_of_middle = i
        else:
            break

    # expand middle array right
    new_end_of_middle = end_of_middle_arr
    for i in xrange(end_of_middle_arr + 1, len(a)):
        if a[i] < a[max_index]:
            new_end_of_middle = i
        else:
            break
    print new_beg_of_middle, new_end_of_middle


# orig array vvv
#array = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
array = [1, 2, 4, 7, 10, 7, 0, 19, 6, 7, 16, 18, 19]
#get_index_range(array)
get_index_range2(array)
