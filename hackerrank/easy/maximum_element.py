#https://www.hackerrank.com/challenges/maximum-element

# this is super sneaky, it takes advantage of the fact that delete isn't
# really the same as pop()... so the new num you push doesn't actually have
# to be the correct value

# ...i had to get help on this after trying unsuccessfully due to performance
# with a stack+heap

import heapq
from sys import maxint

stack = []

num_commands = int(raw_input())

def cmd1(args):
    new_elem = args[1]
    existing_max = stack[len(stack)-1] if len(stack) else (-maxint - 1)
    stack.append(max(new_elem, existing_max))

def cmd2(args):
    popped_elem = stack.pop()
    
def cmd3(args):
    max_elem = stack[len(stack)-1]
    print '%s' % str(max_elem)

for i in xrange(num_commands):
    cmd = map(int, raw_input().split(' '))
    func_dict = {1:cmd1, 2:cmd2, 3:cmd3} # cool switch statement trick
    func_dict[cmd[0]](cmd)
