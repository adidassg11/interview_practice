# https://www.hackerrank.com/challenges/maxsubarray
# status - partial complete - 2nd test case taking 7seconds
# time started - 2:15pm
# time started - 3:22pm

num_tests = int(raw_input().strip())

for t in xrange(num_tests):
    a_size = int(raw_input().strip())
    a = [int(x) for x in raw_input().strip().split()]
    
    sums = []
    max_sum = (0, 0, a[0]) #i, j, sum
    largest_negative = None
    largest_total_sum = None
    #import pdb; pdb.set_trace()
    for i in xrange(a_size): #i is the start point
        if a[i] < 0:
            if not largest_negative:
                largest_negative = a[i]
            else:
                if a[i] > largest_negative:
                    largest_negative = a[i]
        else:
            if not largest_total_sum:
                largest_total_sum = a[i]
            else:
                largest_total_sum += a[i]
        for j in xrange(a_size-i):
            #print "j: %s" % j
            if j == 0:
                sums.append([a[i+j]])
                if a[i] > max_sum[2]:
                    max_sum = (i, j, a[i])
            else:
                new_sum = sums[i][j-1] + a[i+j]
                sums[i].append(new_sum)
                if new_sum > max_sum[2]:
                    max_sum = (i, j, new_sum)
                    #print 'new maxsum: ' , max_sum

    '''
    # O(nlogn), can we do better??
    # sol'n -> keep track of largest negative number in the above algo
    # just add all positive numbers, or use largest negative
    a.sort()
    a.reverse()
    # ignore negatives
    best_sum_overall = a[0]
    for i in xrange(1, a_size):
        if a[i] > 0:
            best_sum_overall += a[i]
    '''

    if not largest_total_sum: # it was only negative numbers
        largest_total_sum = largest_negative
    #print max_sum[2], best_sum_overall
    print max_sum[2], largest_total_sum

    # KADANES ALGO O(n) vvvv
    total_sum = a[0] #TODO
    local_sum = a[0]
    for x in a[1:]:
        if local_sum + x > 0:
            local_sum += x
            if local_sum > total_sum:
                total_sum = local_sum


            
