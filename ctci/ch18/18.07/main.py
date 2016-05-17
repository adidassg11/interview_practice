#!/usr/bin/python

# start: 6:15
# finish: 7:21 (without many tests)
# status: complete (not very tested)
# solution: recursion O(len(word)*len(word_list)) time and mem (could potentially have a huge recursive call stack with small 2 letter words), however real words have a reasonable size limit so it's largely impacted by the length of the word list, this could be a whole conversation just about the runtime

def sortByLength(word_list):
    """
        Make a list form longest word first to smallest last

        O(n) runtime O(n) mem NOTE: this could be done better
    """
    longest_word_len = 0
    word_len_dict = {} # { len: [word1, word2, ...] }
    for word in word_list:
        wlen = len(word)
        if wlen > longest_word_len:
            # This is sort of a cheap way to do this.. could use max heap
            # instead of the for loop to find next largest len...
            longest_word_len = wlen

        if wlen in word_len_dict:
            same_len_list = word_len_dict[wlen]
            same_len_list.append(word)
        else:
            word_len_dict[wlen] = [word]

    new_word_list = [] # this is the sorted list from largest to smallest len
    for i in xrange(longest_word_len, 0, -1):
        if i in word_len_dict:
            new_word_list.extend(word_len_dict[i]) 

    #DEBUG
    print new_word_list

    return new_word_list
    
def isFromWordSet(word, word_set):
    #print 'isFromWordSet(%s)' % word
    if word in word_set:
        return True
    else:
        # Try all of these combinations
        for i in xrange (1, len(word)):
            if isFromWordSet(word[0:i], word_set):
                if isFromWordSet(word[i:], word_set):
                    return True
        return False

def longestCompositeWord(word_list):
    word_set = {word for word in word_list}
    word_list = sortByLength(word_list)

    for word in word_list:
        #print 'checking for longest word: %s' % word
        word_set.remove(word) # could do this remove/add or pass flag to ignore
        if isFromWordSet(word, word_set):
            print 'found longest word: %s' % word
            return word
        word_set.add(word)

    print 'No composite words found'
    return 'No composite words found'

#words = ['cat', 'banana', 'dog', 'nana', 'walk', 'walker', 'dogwalker']
#words = ['cat', 'banana', 'dog', 'nana', 'walk', 'walker', 'er']
words = ['cat', 'banana', 'dog', 'nana', 'walk', 'walker', 'catdognana']
longestCompositeWord(words)
words = ['cat', 'banana', 'dog', 'nana', 'walk', 'walker', 'catdognanaX']
longestCompositeWord(words)
words = ['cat', 'banana', 'dog', 'nana', 'walk', 'walker', 'catdognanax', 'x']
longestCompositeWord(words)
words = ['cat', 'banana', 'dog', 'nana', 'walk', 'walker', 'catdognanax', 'X']
longestCompositeWord(words)
words = ['cat', 'banana', 'dog', 'nana', 'walk', 'walker', 'catdognanaXX', 'X']
longestCompositeWord(words)
