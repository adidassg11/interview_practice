#!/usr/bin/python

# status - WIP
# start - 1155
# end - 1120
# solution O(k^2/2), how do i do this in linear time???

def generate_lengths(k):
    if k == 0:
        return 0

    possible_lengths = set()
    possible_lengths.add('k')
    possible_lengths.add('s')

    for i in xrange(k-1):
        #TODO: lots of duplicate checks, need shortcut for eliminating,
        # could base it on length of 'length' and the iteration #
        for length in possible_lengths:
            new_set = possible_lengths.copy()
            new_length = ''.join(length + 's')
            if new_length not in new_set:
                new_set.add(new_length)
            new_length = ''.join('k' + length)
            if new_length not in new_set:
                new_set.add(new_length)
            possible_lengths = new_set.copy()
    
    print possible_lengths
    return len(possible_lengths)


#there is a clear pattern here, you could just hard code some math but that's not as flexible when you want to add new length possibilities...
#print generate_lengths(1)
#print generate_lengths(2)
print generate_lengths(3)
'''
print generate_lengths(4)
print generate_lengths(5)
print generate_lengths(6)
'''

