#!/usr/bin/python

# status - incomplete, WIP
# start - 1155
# end - 1220
# solution O(k^2/2), how do i do this in linear time???

#trying again:
# start - 1110
# end - 1116
# solution: O(k) runtime

class BadArgumentsException(Exception):
    pass

# Insight - order/combo doesn't matter. This is actually really trivial
def generate_lengths2(k, longer_len='L', shorter_len='S'):
    if k == 0:
        raise BadArgumentsException

    lengths = set()  # avoids multiple lengths of same size
    for i in range(k+1):
        new_len = shorter_len*i + longer_len*(k-i)
        lengths.add(new_len)

    return lengths


# this was my original but i misread the question
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
print generate_lengths2(1)
print generate_lengths2(2)
print generate_lengths2(4)
print generate_lengths2(4, 5, 2)
print generate_lengths2(4, 1, 1)
# print generate_lengths(5)
# print generate_lengths(6)

