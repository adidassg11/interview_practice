# note: this is written for python3

from collections import defaultdict

ordered_coin_vals = [
    {'value': 1, 'name': 'P'},
    {'value': 5, 'name': 'N'},
    {'value': 10, 'name': 'D'},
    {'value': 25, 'name': 'Q'},
]

def clean_print(coins):
    # TODO: super clean way would be to tie this to ordered_coin_vals to avoid going out of sync
    cc = defaultdict(int)  # Coin counts
    for coin in coins:
        cc[coin] += 1

    print('%s Quarters %s Dimes %s Nickels %s Pennies' % (cc['Q'], cc['D'], cc['N'], cc['P']))


# Slow AF around 49 (over 1M combs), maybe there are repeats, try with set...
def ways_to_make_change1(max_price):
    change_combs = {0: ['']}  # combinations to make change for a given price e.g. 5: ['N', 'PPPPP']

    for price in range(1, max_price+1):
        print('Price: %s' % price)
        new_price_combs = []

        for coin in ordered_coin_vals:
            if price-coin['value'] in change_combs:
                for comb in change_combs[price-coin['value']]:
                    #new_price_comb = ''.join(sorted(comb + coin['name']))
                    new_price_comb = ''.join(comb + coin['name'])
                    new_price_combs.append(new_price_comb)

        change_combs[price] = new_price_combs

        print('combinations: %s' % len(change_combs[price]))

        if price == 100:
            print('combs for %s cents: %s' % (price, new_price_combs))


# Huge speedup, num combinations is in the 3 digits range, not millions. Set avoids repeats
def ways_to_make_change2(max_price):
    change_combs = {0: set(' ')}  # combinations to make change for a given price e.g. 5: ['N', 'PPPPP']

    for price in range(1, max_price+1):
        new_price_combs = set()

        for coin in ordered_coin_vals:
            if price-coin['value'] in change_combs:
                for comb in change_combs[price-coin['value']]:
                    new_price_comb = ''.join(sorted(comb + coin['name']))  # TODO: give a key function to sort by QNDP order... can just use bash sort on output tho...
                    new_price_combs.add(new_price_comb)

        change_combs[price] = new_price_combs

        if price == 100:
            # sort my set
            sorted_list = [x for x in new_price_combs]  # TODO: Way to use map here?
            max_len = 0
            for x in sorted_list:
                max_len = max(max_len, len(x))
            for comb in new_price_combs:
                clean_print(comb)

def ways_to_make_change(price):
    #return ways_to_make_change1(price)
    return ways_to_make_change2(price)

ways_to_make_change(100)
