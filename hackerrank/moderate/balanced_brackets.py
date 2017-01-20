# balanced brackets
# https://www.hackerrank.com/challenges/balanced-brackets

#!/bin/python

import sys

opens = '({['
closes = ')}]'
pairs = { o:c for o,c in zip(opens,closes) }

def is_balanced(s):
    stack = []
    for char in s:
        if char in opens:
            stack.append(char)
        elif char in closes:
            if len(stack) < 1 or pairs[stack.pop()] != char:
                return False
            continue
        else:
            return False # bad character
     
    return not stack


t = int(raw_input().strip())
for a0 in xrange(t):
    s = raw_input().strip()
    
    print 'YES' if is_balanced(s) else 'NO'
