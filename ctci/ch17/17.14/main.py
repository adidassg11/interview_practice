#!/usr/bin/python

# status - INCOMPLETE

def optimizeSentence(words):
    # recursively split the sentence(s) and optimize
    # do another pass to combine words and/or dangling letters (denoted by only having 1 space instead of 2)
    if words in global_dict:
        new_words = ' ' + words + ' '
        return (new_words, False, 0, 0) #TODO: not sure where to go with this yet...
    #else:
    #    return (new_words, True, 0, 1) # TODO: True means need more processing, indicies defines range
    else:
        # There is more to process, need to find split points and process them

        len_words = len(words)
        # good_idx is point up until which things have been parsed, left or right matters
        new_words_left, needs_proc1, proc_start1, proc_end1 = optimizeSentence(words[:len_words/2]) 
        new_words_right, needs_proc2, proc_start2, proc_end2 = optimizeSentence(words[len_words/2+1:])
        new_words = ''
        if needs_proc1:
            new_words += new_words_left[proc_start1:proc_end1]
        if needs_proc2:
            new_words += new_words_right[proc_start2:proc_end2]

        for word in new_words:
            if 

#TODO: add didn't
# implement as set
global_dict = {'i', 'reset', 'the', 'computer', 'it', 'still', 'boot', 'looked', 'just', 'like', 'her', 'brother', 'extra', 'words'}
test1 = 'jesslookedjustliketimherbrother'
optimizeSentence(test1)
