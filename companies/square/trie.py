#!/usr/bin/python
    
class Trie():
    #children = [] #TODO: not array!
    def __init__(self, letter):
        self.letter = letter
        self.children = []  # use O(1) dict
    
    # def __str__(self):
    #     #children = for 
    #     child_strings = ''
    #     for c in self.children:
    #         child_strings = c.__str__
    #     return '%s' % (self.letter + child_strings)
    
    def insertWord(self, word):
        print word, len(self.children)
        need_new_trie = True
        for c in self.children:
            if word[0] == c.letter:
                if len(word) > 1:
                    c.insertWord(word[1:])
                need_new_trie = False
            
        if need_new_trie:
            # found unique letter
            trie = Trie(word[0])
            self.children.append(trie)

            if len(word) > 1:
                trie.insertWord(word[1:])
            
    def getUniquePrefix(self, word):
        print word, len(self.children)
        if len(self.children) <= 1:
            return self.letter
        
        for t in self.children:
            if t.letter == word[0]:
                if len(word) > 1:
                    return self.letter + t.getUniquePrefix(word[1:])
                else:
                    return word[0]
        
    
trie = Trie(' ')
words = ['simple', 'single', 'solution', 'a']
for w in words:
    trie.insertWord(w)

print trie
unique_prefixes = []

for w in words:
    unique_prefixes.append(trie.getUniquePrefix(w))

print unique_prefixes
    


# 
# Your previous Plain Text content is preserved below:
# 
# 
# inputs           outputs
# simple           sim
# single           sin
# solution         so
# a                a
# 
# xyz
# xyw
# xya
# add simple to map
# 
# Sal is here

