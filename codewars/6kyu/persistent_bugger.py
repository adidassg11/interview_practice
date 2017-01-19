def is_complete(num):
    return True if num < 10 else False

def persistence(n):
    pers = 0 # persistence means number of iterations
    print 'str(n): %s' % str(n)

    while not is_complete(n):
        new_num = 1
        for digit in str(n):
            print 'str(n): %s' % str(n)
            new_num *= int(digit)
        n = new_num
        pers += 1
        
    return pers

assert(persistence(39) == 3)
assert(persistence(4) == 0)
assert(persistence(25) == 2)
assert(persistence(999) == 4)

