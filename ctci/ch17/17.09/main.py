#!/usr/bin/python
# status - complete? need to check solution

'''
Answer:
This is too easy so it must be an open ended design consideration sort of question. 

Trivial situation is to have a dictionary that you just keep increasing the values for dict keys

Questions to consider:
- handling certain words (like plurals, typos, proper nouns, hyphenated things, capitalization, etc.)
- If the dictionaries will be huge, maybe we should break the words up by first letter or something??
- Maybe we build it up in a multithreaded fashion? run the task in the background with low priority (nice)
'''
