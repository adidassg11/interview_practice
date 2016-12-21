#!/usr/bin/python

# status - complete with one tiny bug with whitespace(maybe more)
# start - 957
# end - 1040
# solution - O(n), O(1) mem

def print_num(num):
    under_twenty_dict = { 0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four',
                  5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
                  10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen',
                   14: 'fourteen', 15: 'fifteen', 16: 'sixteen',
                   17: 'seventeen', 18: 'eighteen', 19: 'nineteen' }
    tens_dict = { 2: 'twenty', 3: 'thirty', 4: 'fourty', 5: 'fifty',
                  6: 'sixty', 7: 'seventy', 8: 'eighty', 9: 'ninety' }
    powers_of_thousand = { 0: '', 1: 'thousand', 2: 'million', 3: 'billion' } # this could keep going...

    
    def get_string_for_three_digits(num):
        num_string = '' 

        # === Start parsing the number === #

        # tens and ones
        final_two = num % 100
        final_two_are_zero = True if final_two == 0 else False

        if final_two < 19:
            if final_two > 0:
                num_string += under_twenty_dict[final_two]
        else:
            ones_place = final_two % 10
            tens_place = final_two / 10
            num_string += tens_dict[tens_place]
            if ones_place != 0:
                num_string += ' %s' % under_twenty_dict[ones_place]

        # hundreds...
        num /= 100
        if num > 0:
            hundreds = num % 10
            if hundreds != 0:
                num_string = under_twenty_dict[hundreds] + ' hundred ' + num_string
                if final_two_are_zero:
                    num_string = num_string[:-1] # delete that extra space if necessary

        return num_string

    num_string = ''

    # zero is a special case
    if num == 0:
        return under_twenty_dict[num]

    # account for negative
    is_negative = False
    if num < 0:
        is_negative = True
        num *= -1

    power_of_thousand = 0

    while num > 0:
        next_three = num % 1000
        num_string = ( get_string_for_three_digits(next_three) +
                       ' %s ' % powers_of_thousand[power_of_thousand] + num_string)
        num /= 1000
        power_of_thousand += 1

    if is_negative:
        num_string = 'negative ' + num_string
    
    return num_string[:-2] # accounts for white spaces at the ends


print print_num(0)
print print_num(15)
print print_num(35)
print print_num(435)
print print_num(999)
print print_num(1999)
print print_num(104600)
print print_num(104601)
print print_num(10422104600)
print print_num(100030000) # bug - has a white space at the end
print print_num(-100030000)
