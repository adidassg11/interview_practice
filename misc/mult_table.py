#! /usr/bin/python

print 'hello'

#   1 2 3 4 5
# 1 1 2 3 4 5
# 2 2 4 6 8 10
# 3 3 6 9 12 15
# 4

width = 10
height = 10

table = []

# solution 1: store in n^2 memory in n^2 time, then print in n^2 time
for x in xrange(1, height+1):
    print x
    new_row = []
    table.append(new_row)
    for y in xrange(1, width+1):
        table[x-1].append(x*y)


for row in table:
    print row

# solution 2: don't use memory

for x in xrange(1, height + 1):
    row_str = ''
    for y in xrange(1, width + 1):
        row_str += '%d ' % (x*y)
    print row_str.rstrip()
