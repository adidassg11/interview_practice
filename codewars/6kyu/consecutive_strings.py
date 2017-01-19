# Link: https://www.codewars.com/kata/56a5d994ac971f1ac500003e/solutions/python

import operator

def longest_consec(strarr, k):
    longest_word = ''

    # Error conditions
    if k <= 0 or k > len(strarr):
        return longest_word

    # build initial word
    longest_word = ''.join(strarr[:k])
        
    for i in xrange(k+1, len(strarr)+1): #prob off by 1 error
        new_word = ''.join(strarr[i-k:i])

        if len(new_word) > len(longest_word):
            longest_word = new_word

    return longest_word



assert(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2) == "abigailtheta")
assert(longest_consec(["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"], 1) == "oocccffuucccjjjkkkjyyyeehh")
assert(longest_consec([], 3) == "")
assert(longest_consec(["itvayloxrp","wkppqsztdkmvcuwvereiupccauycnjutlv","vweqilsfytihvrzlaodfixoyxvyuyvgpck"], 2) == "wkppqsztdkmvcuwvereiupccauycnjutlvvweqilsfytihvrzlaodfixoyxvyuyvgpck")
assert(longest_consec(["wlwsasphmxx","owiaxujylentrklctozmymu","wpgozvxxiu"], 2) == "wlwsasphmxxowiaxujylentrklctozmymu")
assert(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], -2) == "")
assert(longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 3) == "ixoyx3452zzzzzzzzzzzz")
assert(longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 15) == "")
assert(longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 0) == "")
