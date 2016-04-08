
def print_tree(n):
    if not n:
        return 'X'
    else:
        print n.data
        print_tree(n.lc)
        print_tree(n.rc)

def build_tree(a, n, parent):
    # Given an array and node, use pre-order traversal to create the binary tree
    parent_data = ''
    if parent:
        parent_data = parent.data
    print 'build tree with args a:%s, n:%s, parent.data:%s' % (a, n.data, parent_data)

    if not len(a):
        return n

    if a[0] < n.data:
        #if parent and #TODO right side of trees
        new_node = Node(a[0])
        a.pop(0)
        print 'building left...'
        n.lc = build_tree(a, new_node, n)
        print 'building right1...'
        n.rc = build_tree(a, new_node, n)
        return n
    else:
        #if parent and a[0] < parent.data:
        new_node = Node(a[0])
        a.pop(0)
        n.rc = build_tree(a, new_node, n)
        return n
    return n #this shouldn't hit
    #TODO: what about equal node vals?? does it go as leaf or up to parent?

