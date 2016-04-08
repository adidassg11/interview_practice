#!/usr/bin/python

class NotFoundException(Exception):
    def __init__(self, message):
        self.message = message

class Node:
    def __init__(self, n, lc=None, rc=None):
        self.data = n
        self.lc = lc # left child
        self.rc = rc # right child

    def __str__(self):
        return "d:%s l:%s r:%s" % (self.data, self.lc.__str__(), self.rc.__str__())

# O(logn)
def insert_into_tree(n, val):
    if val < n.data:
        if n.lc:
            insert_into_tree(n.lc, val)
        else:
            new_node = Node(val)
            n.lc = new_node
    else:
        if n.rc:
            insert_into_tree(n.rc, val)
        else:
            new_node = Node(val)
            n.rc = new_node

def build_path_to_node(n, target, a):
    if not n:
        raise NotFoundException('Not found')

    if n.data == target:
        a.append(n.data)
        return
    elif target < n.data:
        a.append(n.data)
        build_path_to_node(n.lc, target, a)
    else:
        a.append(n.data)
        build_path_to_node(n.rc, target, a)


## START ##
num_tests = int(raw_input().strip())

for t in xrange(num_tests):
    # Parse and clean the data input
    a = int(raw_input().strip())
    b = int(raw_input().strip())
    data = [int(x) for x in raw_input().strip().split()]

    t = Node(data[0])
    #build_tree(data[1:], t, None)
    for x in data[1:]:
        insert_into_tree(t, x)
    path_to_a = []
    path_to_b = []
    try:
        build_path_to_node(t, a, path_to_a)
        build_path_to_node(t, b, path_to_b)
    except NotFoundException as e:
        print 'Not found'
        continue

    #print 'apath: ', path_to_a
    #print 'bpath: ', path_to_b

    # now simply walk through the paths and find the split point
    i = 0
    while i < min(len(path_to_a), len(path_to_b)):
        if path_to_a[i] == path_to_b[i]:
            #print 'paths equal'
            i += 1
            continue
        else:
            # paths split
            break

    # i is least common ancestor (LCA)
    # dist = distA to LCA + distB to LCA
    distance = (len(path_to_a) - i) + (len(path_to_b) - i)
    print distance
    
