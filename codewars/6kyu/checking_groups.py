#!/usr/bin/python

#status - Brute force O(n^2) working, need to do better with stack O(n)

"""
http://www.codewars.com/kata/54b80308488cb6cd31000161/train/python

In English and programming, groups can be made using symbols such as "()" and "{}" that change meaning. However, these groups must be closed in the correct order to maintain correct syntax.

Your job in this kata will be to make a program that checks a string for correct grouping. For instance, the following groups are done correctly:

({})
[[]()]
[{()}]

The next are done incorrectly

{(})
([]
[])

"""

# complementary character, only find closing chars for now
comp_char = {'(':')', '[':']', '{':'}'}

def is_valid_group(s):
    if not s:
        return False

    # This assumes we're only using the group chars, nothing added
    if len(s) % 2:
        return False

    # Base case
    if len(s) == 2:
        if s[0] in comp_char and comp_char[s[0]] == s[1]:
            return True

    # Recurse
    

def check_brute(s):
    def process_string(s):
        """ check whether we should continue with this processing, may modify string"""
        seeking_char = s[0]
        num_open_char = 1
        num_close_char = 0
        for i in xrange(1, len(s)):
            if s[i] in comp_char:
                num_open_char += 1
            elif s[i] in comp_char.values(): #is this O(1) lookup?
                num_close_char += 1
    
            if num_open_char == num_close_char:
                # candidate for finding a match
                if s[0] in comp_char and comp_char[s[0]] == s[i]:
                    # remove the chars from the group
                    if i == len(s) - 1:
                        new_string = s[:-1]
                    else:
                        #new_string = s[:i-1] + s[i+1:]
                        new_string = s[:i] + s[i+1:]
                    # remove first char
                    new_string = new_string[1:]
                    print 'new string is %s after removing %s and %s at index 0 and %s' % (new_string, s[0], s[i], i)
                    return new_string, True

            # Didn't find a match
            if i == len(s) - 1:
                print 'no match'
                return s, False

            # Else continue processing
        
    if not len(s):
        return True

    #loop_break = 0 # DEBUG
    while len(s) > 0:
        #loop_break += 1
        #if loop_break > 5:
        #    return False
        if len(s) % 2:
            return False
        s, found_match = process_string(s)
        #print 'string is %s after processing' % s
        if found_match:
            if len(s):
                # still more to process
                continue
            else:
                # processed the whole string
                return True
        #else
        return False
    return False
                    

def group_check(s):
    print s
    return check_brute(s)    
