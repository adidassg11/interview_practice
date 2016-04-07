#!/usr/bin/python
# start 8:33am 9:15
# end: 8:40, 9:36 total time: 28min
# status
# solution O(n^2) time, O(n) mem


#TODO: design for x's and o's, also design for NxN board
# assume 3x3 for now and just x's
# also, just use new memory for this insetad of getting fancy and replacing the board data
def hasWon(a, n):
    # Takes array a
    for player in ['x', 'o']:
        diag_possible_so_far = [True]*2 #[0] is down right, and [1] is down left
        col_possible_so_far = [True]*n #possible rows that win
        for r in xrange(n):
            row_possible_so_far = True
            for c in xrange(n):
                # loop thur columns in row 
                #check row
                if row_possible_so_far:
                    if a[r][c] == player:
                        if c == n-1:
                            return True #and return 'x'?
                    else:
                        row_possible_so_far = False
                #check column
                if col_possible_so_far[c]:
                    if a[r][c] == player:
                        if r == n-1:
                            return True
                    else:
                        col_possible_so_far[c] = False
                #check diagonal
                if r == c:
                    if diag_possible_so_far[0]:
                        if a[r][c] == player:
                            if r == n-1:
                                return True
                        else:
                            diag_possible_so_far[0] = False
                if r == n-c-1:
                    if diag_possible_so_far[1]:
                        if a[r][c] == player:
                            if r == n-1:
                                return True
                        else:
                            diag_possible_so_far[1] = False
             
    return False

#game1 = [['o','o','o'],['x','x','x'],['o','o','o']]
#game2 = [['o','o','x'],['o','o','x'],['o','o','x']]
game1 = [['-','-','-'],['x','x','x'],['-','-','-']]
game2 = [['-','-','x'],['-','-','x'],['-','-','x']]
game3 = [['-','-','x'],['-','x','-'],['x','-','x']]
game4 = [['-','-','x'],['-','x','-'],['0','-','x']]
game5 = [['-','-','-','x'],['-','-','x','-'],['-','x','-','-'],['x','-','-','-']]
game6 = [['x']]
game7 = [['-']]
game8 = [['-','-','-'],['o','o','o'],['-','-','-']]
print hasWon(game1, 3)
print hasWon(game2, 3)
print hasWon(game3, 3)
print hasWon(game4, 3)
print hasWon(game5, 4)
print hasWon(game6, 1)
print hasWon(game7, 1)
print hasWon(game8, 3)
