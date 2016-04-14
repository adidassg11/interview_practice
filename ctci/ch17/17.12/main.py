#!/usr/bin/python
#start - 2:40 am
#end -  3:08 am
#status - complete
#solution - O(n) with O(n) memory or O(nlogn) with const mem, ignores duplicates


#a is array, s is sum
def find_pairs(a, s):
    find_pairs1(a, s)

# O(nlogn) sort then move inwards from the max and min of the array
def find_pairs1(a, s):
    a = sorted(a)

    ans = []
    i = 0
    j = len(a) - 1
    while j>i:
        #print 'i:%s j:%s' % (i, j)
        # Found answer, store it
        if a[i] + a[j] == s:
            ans.append((a[i], a[j]))
            i += 1
            j -= 1
        elif a[i] + a[j] > s:
            j -= 1
        else:
            i += 1

    print ans

# O(n) and O(n) memory store a dictionary as we go along
# ignore duplicates
def find_pairs2(a, s):
    ans = []
    arr_set = set()
    arr_set = { x for x in a }
    for x in [ x for x in a if x < max(a)/2]:
        if s-x in arr_set:
            ans.append((x, s-x))
    print ans
            

array = [1, 2, 3, 4, 5, 6]
find_pairs(array, 5) #should be 1-4 and 2-3
find_pairs(array, 0) #should be []
find_pairs(array, 1) #should be []
