#!/usr/bin/python
# start time - 2:26
# end time - 
# status - complete with some bugs
# solution - O(n^2) cpu and O(n^2/2) mem to build dict then O(1) lookup

#NOTE: this assumes no punctuation, text has already been cleansed

import copy

#TODO: can use dynamic programming to build up a dict of dict {word1:{word2:distance}} to store distances
def find_shortest_path(text, word1, word2):
    #return find_shortest_path_brute(text, word1, word2)
    return find_shortest_path_memoize(text, word1, word2)

'''
This mostly works
Known bugs:
- using the same word when there is only 1 occurance
'''
def find_shortest_path_brute(text, word1, word2):
    print 'word1:%s word2:%s' % (word1, word2)
    def get_other_word(word):
        return word2 if word == word1 else word1
        ''' # this is correct because of PEP20 zen of python?
        if word == word1:
            return word2
        else:
            return word1
        '''

    split_text = text.split()
    shortest_path = len(split_text)
    last_pos = 0
    cur_pos = 0
    first_word = None 
    next_word = None
    first_word_index = 0
    idx1 = 0
    idx2 = 0

    #for word in split_text:
    for i in xrange(len(split_text)):
        word = split_text[i]
        #print 'i: %s word: %s' % (i, word)
        if not first_word:
            #print 'looking for first word'
            # Need to find a match before we can start finding distance
            if word in (word1, word2):
                #indecies
                first_word = word
                next_word = get_other_word(word)
                first_word_index = i
                idx1 = i
                #print 'found match, first word: %s, second word: %s' % (first_word, next_word)
            #else:
                #print 'no match'
        else:
            if word == first_word:
                #print 'found first_word %s' % word
                first_word = word
                first_word_index = i
                idx1 = i
                next_word = get_other_word(word)
            elif word == next_word:
                #print 'found word == %s' % word
                distance = i - first_word_index
                if distance < shortest_path:
                    #if updated, update the indexes of the shortest path
                    idx1 = first_word_index
                    idx2 = i
                first_word = word
                first_word_index = i
            else:
                continue


    shortest_path = abs(idx1-idx2)
    print 'find_shortest_path(), dist:%s, index1:%s, index2:%s' % (shortest_path, idx1, idx2)


path_dict = {}

# Return the words in alphabetical order
def get_ordered_words(word1, word2):
    return (word1, word2) if word1 < word2 else (word2, word1)

def update_dict(key, val, dist):
    print 'update_dict(%s, %s, %s) ' % (key, val, dist)
    if key not in path_dict:
        print 'key not in dict'
        path_dict[key] = {val: dist}
    else:
        if val not in path_dict[key]:
            print 'val not in dict'
            path_dict[key][val] = dist
        else:
            print 'key and val in dict, setting dist'
            path_dict[key][val] = min(path_dict[key][val], dist)

def get_distance(word1, word2):
    first_word, second_word = get_ordered_words(word1, word2)
    distance = path_dict[first_word][second_word]
    return distance

def build_path_dict(text):
    print 'build_path_dict'

    #NOTE: we can use .lower() or leave it out, just depends on the spec.
    text_split = text.lower().split()
    #text_split = text.split()
    text_len = len(text_split)

    # loop thru word combinations
    for idx1 in xrange(0, text_len):
        word1 = text_split[idx1]
        print 'word1: %s' % text_split[idx1] 
        text_split.pop(idx1)
        print 'the rest of the list: %s' % text_split
        for idx2 in xrange(0, text_len - 1):
            word2 = text_split[idx2]
            print 'word2: %s' % text_split[idx2] 
            # Insert/update dictionary with distances
            # The key will be whichever word is first alphabetically
            distance = abs(idx2 - idx1)
            #key, val = (word1, word2) if word1 < word2 else (word2, word1)
            key, val = get_ordered_words(word1, word2)
            #TODO: there is a better way to do this
            #TODO: include indexes in the value, not just distance
            update_dict(key, val, distance + 1) #TODO: distance off by one because of pop(), no?

        text_split.insert(idx1, word1)

'''
Solution:
Need to create
m is 13th letter, n is 14th
O(n^2) to build, O(n^2) mem
'''
def find_shortest_path_memoize(text, word1, word2):
    #print 'find_shortest_path_memoize'
    if not len(path_dict):
        build_path_dict(text)
        print path_dict
        
    distance = get_distance(word1, word2)
    print 'distance between %s and %s is %s' % (word1, word2, distance)
    return distance


text = 'You have a large text file containing words. Given any two words, find the shortest distance (in terms of number of words) between them in the file. If the operation will be repeated many times for the same file (but different pairs of words), can you optimize your solution'

#text = 'You have a large'

text = text.lower()
find_shortest_path(text, 'have', 'a')
#find_shortest_path(text, 'a', 'have')
#find_shortest_path(text, 'a', 'a')
#find_shortest_path(text, 'You', 'large')
find_shortest_path(text, 'you', 'large')
#find_shortest_path(text, 'file', 'the')

