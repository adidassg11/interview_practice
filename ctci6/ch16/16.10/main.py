#!/usr/bin/python

# status - wip
# start - 1111 (but i totally cheated and thought about it before coding)
# end - 1138
# solution - O(n) run time with constant array size, we could make that variable and it would affect run time complexity

from collections import defaultdict

def years_brute(l):
    num_alive = defaultdict(int)
    for x,y in l:
        for year in xrange(x, y+1):
            num_alive[year] += 1

    year_of_max_alive = -1
    max_alive = 0

    for year, num_alive in num_alive.items():
        if num_alive > max_alive:
            year_of_max_alive = year
            max_alive = num_alive

    print year_of_max_alive, max_alive

def years_better(l):
    years_list = [0] * 101 # year 1900 is years_list[0]

    for birth, death in l:
        print birth, birth-1900
        years_list[birth-1900] += 1
        print death, death-1900
        if death < 2000:
            years_list[death-1900+1] -= 1 # the +1 because you include their death year as being alive

    total_alive = 0
    max_alive = 0
    max_alive_year = -1

    for year in xrange(101):
        alive_delta = years_list[year]
        total_alive += alive_delta 
        if total_alive > max_alive:
            max_alive = total_alive
            max_alive_year = 1900 + year
    print years_list
    print max_alive, max_alive_year


def year_with_most_alive(l):
    #years_brute(l) 
    years_better(l) 

#years = [(1900, 1901), (1901, 1902), (1903, 1998), (1999, 2000)] #1901 - 2 people
#years = [(1900, 1901), (1901, 1902), (1903, 1999), (1998, 1999), (1999, 2000)] # 1999 - 3 people
years = [(1900, 1901), (1901, 1902), (1903, 1999), (1998, 1999), (1999, 2000), (1904, 1904), (1904, 1904), (1904, 1904)] # 1904 - 4 people

year_with_most_alive(years)
