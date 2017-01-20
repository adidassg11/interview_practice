#!/bin/python

class Coord(object):
    start_x = None #bad name, keep for simplicity
    start_y = None
    next_x = None
    next_y = None
    size_x = None
    size_y = None
    lbx = None#left boundary x
    rbx = None
    tby = None #top boundary y
    bby = None 
    # ... others, need global matrix size to compute these
    def __init__(self, start_x, start_y, matrix_size_x, matrix_size_y):
        self.start_x = start_x
        self.start_y = start_y
        self.size_x = matrix_size_x
        self.size_y = matrix_size_y

    def __repr__(self):
        return 'Coord repr unavailable'

    def __str__(self):
        #return '%s,%s->%s,%s, lbx:%s rbx:%s tby:%s bby:%s' % (self.start_x, self.start_y, self.next_x, self.next_y, self.lbx, self.rbx, self.tby, self.bby)
        return '%s,%s->%s,%s' % (self.start_x, self.start_y, self.next_x, self.next_y)

    def __compute_boundaries(self):
        if self.size_x == None or self.size_y == None:
            raise Exception('self.size_x and/or size_y not defined')

        # Get boundary lines along which coord will travel when rotated
        min_dist_from_x_edge = min(self.start_x, self.size_x-1-self.start_x)
        min_dist_from_y_edge = min(self.start_y, self.size_y-1-self.start_y)
        min_dist_from_edge = min(min_dist_from_x_edge, min_dist_from_y_edge)
        self.lbx = min_dist_from_edge 
        self.rbx = self.size_x - min_dist_from_edge - 1 #TODO test for small matrix
        self.tby = min_dist_from_edge
        self.bby = self.size_y - min_dist_from_edge - 1

    def get_next_rotate_pos(self):
        print 'in get_next_rotate_pos()...'
        if self.lbx == None or self.rbx or self.tby or self.bby == None:
            self.__compute_boundaries()

        if self.next_x == None and self.next_y == None:
            self.next_x = self.start_x
            self.next_y = self.start_y
        else:
            return (self.next_x, self.next_y)

        # Corners first
        if self.start_x == self.lbx and self.start_y == self.tby:
            if self.next_y + 1 <= self.bby:
                self.next_y += 1
        elif self.start_x == self.lbx and self.start_y == self.bby:
            if self.next_x + 1 <= self.rbx:
                self.next_x += 1
        elif self.start_x == self.rbx and self.start_y == self.bby:
            if self.next_y -1 >= self.tby:
                self.next_y -= 1
        elif self.start_x == self.rbx and self.start_y == self.tby:
            if self.next_x - 1 >= self.lbx:
                self.next_x -= 1
        else:
            # edges that aren't corners
            if self.start_x == self.lbx:
                self.next_y += 1
            if self.start_x == self.rbx:
                self.next_y -= 1
            if self.start_y == self.tby:
                self.next_x -= 1
            if self.start_y == self.bby:
                self.next_x += 1
        return (self.next_x, self.next_y)

    def printInfo(self):
        if self.next_x == None or self.next_y == None:
            self.get_next_rotate_pos()
        print '%s,%s->%s,%s' % (self.start_x, self.start_y, self.next_x, self.next_y)

    def getNextCoords(self):
        if self.next_x == None or self.next_y == None:
            self.get_next_rotate_pos()
        return (self.next_x, self.next_y)
