#!/usr/bin/python

# status: WIP
# start: 1020pm
# end: 1045 taking break, recognized as recursion problem
# notes: literally too hard for my brain to comprehend

import sys
from collections import defaultdict

def debug(args):
    print(args)
    pass


''' so the trick here is to find repetition in the pattern
    to know how to break down the string...
    guaranteed to have a pattern after max 3 characters
    greedy algorithm can fail in some cases here...
    different idea: count letters and use ratios... okay might be problematic
'''
def is_match1(pattern, string):
    if len(pattern) < 3:
        return True

    pattern_chars = defaultdict(int)
    string_chars = defaultdict(int)

    for c in pattern:
        pattern_chars[c] += 1

    for c in string:
        string_chars[c] += 1

    a_b_ratio = float(pattern_chars['a'])/pattern_chars['b']

    debug('patterndict: %s' % pattern_chars)
    debug('stringdict: %s' % string_chars)
    debug('ratio: %s' % a_b_ratio)
    
    return False

def is_match2_help(pattern, string):
    debug('%s pattern: %s string: %s' % (sys._getframe().f_code.co_name, pattern, string))
    is_match = False
    combs = []  #TODO: make this a set

    if len(pattern) < 1 or len(string) < 1:
        return (False, combs)

    if len(pattern) == 1 and len(string) > 0:
        combs.append((pattern, string))
        return (True, combs)

    if len(pattern) == 2 and pattern[0] == pattern[1]:
        # aa or bb, see if string can be split into equal halves
        first_half = string[:len(string)/2]
        second_half = string[len(string)/2:]
        debug('first second: %s %s' % (first_half, second_half))
        if first_half == second_half:
            return (True, [(pattern, first_half)])
        else:
            return (False, [])

    #TODO TEST
    #else too big, recurse
    # combinations with different patterns
    local_is_match = None
    locals_is_match, new_combs = is_match2_help(pattern[1:], string)
    if local_is_match:
        is_match = True
        combs.extend(new_combs)

    local_is_match, new_combs = is_match2_help(pattern[:-1], string)
    if local_is_match:
        is_match = True
        combs.extend(new_combs)

    # combinations with different strings
    local_is_match, new_combs = is_match2_help(pattern, string[1:])
    if local_is_match:
        is_match = True
        combs.extend(new_combs)

    local_is_match, new_combs = is_match2_help(pattern, string[:-1])
    if local_is_match:
        is_match = True
        combs.extend(new_combs)

    return (is_match, combs)


def is_match2(pattern, string):
    combs = [] # possible combinations for a:b pairs

    is_match, new_combs = is_match2_help(pattern, string)

    if is_match:
        combs.extend(new_combs)

    # TODO: now need to go through a:b pairs to see if we can build the string

    return is_match, combs


#assert(is_match('aabab', 'catcatgocatgo'))
#assert(is_match('aabab', 'casstcasstgocasstgo'))
#assert(is_match('aabab', 'casstcasstggoocasstggoo'))
''' all good here vvv
debug('%s %s' % is_match2('a', 'asdf'))
debug('%s %s' % is_match2('b', 'asdf'))
debug('%s %s' % is_match2('bb', 'asas'))
debug('%s %s' % is_match2('aa', 'asas'))
debug('%s %s' % is_match2('aa', 'assa'))
debug('%s %s' % is_match2('aa', 'asfffasfff'))
debug('%s %s' % is_match2('ab', 'asfffasfff'))
debug('%s %s' % is_match2('aa', ''))
'''
debug('%s %s' % is_match2('ab', '1234'))
