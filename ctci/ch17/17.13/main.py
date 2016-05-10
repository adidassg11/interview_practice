#!/usr/bin/python
#start - 6:48am
#end -
#status - incomplete, in progress
# solution - 

class Binode():
    def __init__(self, data=0, node1=None, node2=None):
        self.d = data
        self.n1 = node1
        self.n2 = node2

    def __str__(self):
        return '(d:%s n1:%s n2:%s)' % (self.d, self.n1, self.n2)

# using this on a tree will just print bottom leftmost node
def printList(n):
    print 'printList()'
    # Find front of list
    prev_node = n
    while prev_node != None:
        if prev_node.n1 == None:
            break
        prev_node = prev_node.n1

    # Front found, now print them out
    counter = 0
    next_node = prev_node
    while next_node:
        print '%s:%s' % (counter, next_node.d)
        next_node = next_node.n2

def print_list(n):
    print 'print_list'
    counter = 0
    while n:
        print '%s:%s' % (counter, n.d)
        n = n.n2

def print_tree_in_order(n):
    #print_tree_in_order_stack(n)

    print 'print_tree_in_order_rec'
    print_tree_in_order_rec(n)

#TODO: not working?
def print_tree_in_order_stack(n):
    print 'print_tree_in_order_stack'
    stack = []
    stack.append(n)

    while len(stack):
        new_n = stack.pop()
        n1 = new_n.n1
        n2 = new_n.n2
        if not n1 and not n2:
            print new_n.d
            continue
        else:
            # continue to grow the stack
            if n2:
                stack.append(n2)
            stack.append(new_n)
            if n1:
                stack.append(n1)

def print_tree_in_order_rec(n):
    if not n:
        return
    if n.n1:
        print_tree_in_order_rec(n.n1)
    print n.d
    if n.n2:
        print_tree_in_order_rec(n.n2)


# could use recursion to move tree to an external list, then pass through that list
# and just connect all the nodes, that's O(n) + O(n) with O(n) external memory
def tree_to_list(n):
    def write_tree_to_list(n, l):
        if n is None:
            return
        write_tree_to_list(n.n1, l)
        l.append(n)
        write_tree_to_list(n.n2, l)

    # Build list of nodes from tree
    mylist = []
    write_tree_to_list(n, mylist)

    # Now fix up the prev and next pointers (n1, n2)
    first_node = mylist[0]
    n = mylist[0]
    n.n1 = None
    while n:
   
        next_node = mylist.pop()
        next_node = None
        if len(mylist):
            next_node = mylist.pop()
        if next_node:
            n.n2 = next_node
        else:
            n.n2 = None
        n = n.n2

    print 'printing converted tree to list'
    print_list(first_node)
    return first_node
    
'''
   6
 3   5
7 9 
'''
n = Binode(5)
n3 = Binode(3)
n7 = Binode(7)
n9 = Binode(9)
n3.n1 = n7
n3.n2 = n9
n2 = Binode(6, n3, n)
#print our big tree
print n2 
'''
smalltree = Binode(5, Binode(3), None)
print smalltree
print_tree_in_order(smalltree)
print_list(n2)
tree_to_list(n2)
'''
