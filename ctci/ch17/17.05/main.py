#!/usr/bin/python
# start: 2:37 pm
# end: 3:00 pm
# status - complete
# solution - O(2n) plus O(2n) memory
# optimizations: could use O(n) memory by manipulating the guess array as we go so that way we don't need a copy...

def get_hits(guess, solution):
    def remove_from_pool(pool, letter):
        if letter not in pool:
            return False
        if pool[letter] == 1:
            pool.pop(letter)
        else:
            pool[letter] -= 1
        return True

    hits, phits = '',''
    solution_extras = {}
    guess_extras = []
    for i in xrange(len(guess)):
        print guess[i], solution[i]
        if guess[i] == solution[i]:
            hits += guess[i]
        else:
            solution_extras[solution[i]] = solution_extras.get(solution[i], 0) + 1
            guess_extras.append(guess[i])

    for g in guess_extras:
        if remove_from_pool(solution_extras, g):
            phits += g
        
    return hits, phits

print get_hits('RGBY', 'GGYR')

