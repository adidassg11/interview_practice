#!/bin/python

import coord
import copy

#STATUS - so close! problem with rows and cols
            
#TODO: finish this
class Matrix(object):
    data = None
    size_x = None
    size_y = None

    def __init__(self):
        pass

    def __repr__(self):
        pass

    def __str__(self):
        pass

    def addRow(row):
        if len(row) != size_x:
            raise Exception('Length of row must be %s' % size_x)
        data.append(row)

def printMatrix(m):
    print 'printing matrix...'
    for rows in m:
        print(' '.join([str(x) for x in rows]))

# Import the matrix
(size_y, size_x, num_rot) = (int(x) for x in raw_input().strip().split())
matrix = []
for i in xrange(size_y):
    row = [int(x) for x in raw_input().strip().split()]   
    matrix.append(row)
printMatrix(matrix)

rotation_map = []
for x in xrange(size_x):
    rotation_map.append([])
    for y in xrange(size_y):
        c = coord.Coord(x, y, size_x, size_y)
        c.printInfo()
        rotation_map[x].append(c)


printMatrix(rotation_map)

# Do work...
'''
old_matrix = None
new_matrix = copy.deepcopy(matrix)

for r in xrange(num_rot):
    old_matrix = copy.deepcopy(new_matrix)
    for x in range(size_x):
        for y in xrange(size_y):
            next_x, next_y = rotation_map[x][y].getNextCoords() 
            new_matrix[next_x][next_y] = old_matrix[x][y]

printMatrix(new_matrix)
'''






