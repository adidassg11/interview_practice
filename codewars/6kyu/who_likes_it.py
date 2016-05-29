#!/usr/bin/python

#status - complete

"""
http://www.codewars.com/kata/5266876b8f4bf2da9b000362/train/python

You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. We want to create the text that should be displayed next to such an item.

Implement a function likes :: [String] -> String, which must take in input array, containing the names of people who like an item. It must return the display text as shown in the examples:

likes [] // must be "no one likes this"
likes ["Peter"] // must be "Peter likes this"
likes ["Jacob", "Alex"] // must be "Jacob and Alex like this"
likes ["Max", "John", "Mark"] // must be "Max, John and Mark like this"
likes ["Alex", "Jacob", "Mark", "Max"] // must be "Alex, Jacob and 2 others like this"
For more than 4 names, the number in and 2 others simply increases.

"""

def likes(names):
    names_len = len(names)
    #TODO: suffix makes this confusing
    suffix = ''
    if names_len in (0, 1):
        suffix = "likes this"
    else:
        suffix = "like this"

    prefix = ''
    if names_len == 0:
        prefix = "no one"
    elif names_len == 1:
        prefix = names[0]
    elif names_len == 2:
        prefix = names[0] + ' and ' + names[1]
    elif names_len == 3:
        prefix = names[0] + ', ' + names[1] + ' and ' + names[2]
    else:
        prefix = names[0] + ', ' + names[1] + ' and %s others' % str(names_len - 2)

    return prefix + ' ' + suffix
