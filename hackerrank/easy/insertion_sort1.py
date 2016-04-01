#!/bin/python

def insertionSort(ar):    
    if len(ar) == 1:
        return

    last_elem = ar[len(ar)-1]
    for i in xrange(len(ar)-1, 0, -1):
        if ar[i-1] > last_elem:
            ar[i] = ar[i-1]
        else:
            ar[i-1] = last_elem
        return

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)
print ar
