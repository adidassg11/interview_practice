#!/usr/bin/python

def myprint(mystr):
  print 'hello %s' % mystr

def swap(inlist, i1, i2):
  temp = inlist[i1]
  inlist[i1] = inlist[i2]
  inlist[i2] = temp

# 3 1 2 1 4
def arrange(inlist, pivot):
    num = inlist[pivot] # number we compare to
    lp = 0 # less-than placement spot
    eps = pivot # equal-to placement start
    epe = pivot # etp end
    gp = len(inlist) - 1

    state = ['lt', 'et', 'gt']

    # dont worry about preserving order
    i = 0
    #import pdb; pdb.set_trace()
    while i<=gp:
        if inlist[i] < num:
            lp+=1
            i+=1
            continue
        elif inlist[i] > num:
            swap(inlist, i, gp)
            gp -= 1
        else: #must be equal to
            if i+1 <= gp:
                swap(inlist, i, i+1)
            i += 1
    print inlist

def test():
    mylist = []
    for i in xrange(10):
        mylist.append(i)
        if i == 2:
            i+=1
    print mylist

def test2():
    mybool = False
    mylist = []
    for i in xrange(10):
        mylist.append(i)
        if i == 2:
            mybool = True
            i-=1
    print mylist

def test3():
    mybool = False
    mylist = []
    end = 10
    for i in xrange(end):
        while i < end:
            mylist.append(i)
            if i == 2:
                mybool = True
                i+=2
            else:
                i+=1
    print mylist

def test4():
    mybool = False
    mylist = []
    i = 0
    end = 10
    while i < end:
        mylist.append(i)
        if i == 2:
            mybool = True
            i+=2
        else:
            i+=1
    print mylist

