#!/usr/bin/python

# problem: Given a pattern and a string - find if the string follows the same pattern Eg: Pattern : [a b b a], String : cat dog dog cat

def isMatch(pattern, string):
    def printAndReturn(match):
        if match == False:
            print "Patterns don't match"
        else:
            print "Patterns match"
        return match
        
    words = string.strip().split()
    if len(pattern) != len(words):
        return printAndReturn(False)

    p_to_w_map = {}
    w_to_p_map = {}
    for i in xrange(len(pattern)):
        if pattern[i] in p_to_w_map:
            if words[i] != p_to_w_map[pattern[i]]:
                return printAndReturn(False)
        else:
            if words[i] in w_to_p_map:
                return printAndReturn(False)
            else:
                p_to_w_map[pattern[i]] = words[i]
                w_to_p_map[words[i]] = pattern[i]

    return printAndReturn(True)


pattern = ['a', 'b', 'b', 'a']
string = 'cat dog dog cat'
isMatch(pattern, string)

pattern = ['a', 'b', 'b', 'c']
string = 'cat dog dog cat'
isMatch(pattern, string)

pattern = ['a', 'b', 'b', 'a']
string = 'cat dog dog cats'
isMatch(pattern, string)

pattern = ['a', 'b', 'b', 'c']
string = 'cat dog dog cats'
isMatch(pattern, string)
