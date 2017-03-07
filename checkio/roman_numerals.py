
ROMANS = (('M',  1000),
          ('CM', 900),
          ('D',  500),
          ('CD', 400),
          ('C',  100),
          ('XC', 90),
          ('L',  50),
          ('XL', 40),
          ('X',  10),
          ('IX', 9),
          ('V',  5),
          ('IV', 4),
          ('I',  1))


def get_roman_numeral(num):
    ret_rn = ''  # Return roman numeral
    remainder = 0
    for roman, arabic in reversed(ROMANS):
        if num >= arabic:
            ret_rn = roman
            remainder = num - arabic
            continue
        break

    return ret_rn, remainder


def checkio(num):
    remainder = 0
    roman_str = ''
    while num > 0:
        (rn, remainder) = get_roman_numeral(num)
        roman_str += rn
        num = remainder
    
    return roman_str

print(checkio(1))
print(checkio(2))
print(checkio(3))
print(checkio(4))

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(6) == 'VI', '6'
    assert checkio(76) == 'LXXVI', '76'
    assert checkio(499) == 'CDXCIX', '499'
    assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'
