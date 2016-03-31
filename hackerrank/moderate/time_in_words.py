#!/bin/python

import sys


h = int(raw_input().strip())
m = int(raw_input().strip())

time_words = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six',
              7:'seven', 8:'eight', 9:'nine', 10:'ten', 11:'eleven',
              12:'twelve', 13:'thirteen', 14:'fourteen',
              15:'quarter', 16:'sixteen', 17:'seventeen', 18:'eighteen',
              19:'nineteen', 20:'twenty', 30:'half'}

def nextHour(h):
    if h == 12:
        return 1
    else:
        return h + 1

def getMinuteWords(m):
    if m <= 20:
        return time_words[m]
    else:
        return "%s %s" % (time_words[20], time_words[m-20])

time_str = ''
if m == 0:
    time_str = "%s o' clock" % time_words[h]
elif m == 15:
    time_str = "quarter past %s" % time_words[h]
elif m == 30:
    time_str = "half past %s" % time_words[h]
elif m == 45:
    time_str = "quarter to %s" % time_words[nextHour(h)]
else:
    minute_str = (m == 1 or m == 59) and 'minute' or 'minutes'
    if m < 30:
        time_str = "%s %s past %s" % (getMinuteWords(m), minute_str, 
                                      time_words[h])
    else:
        time_str = "%s %s to %s" % (getMinuteWords(60-m), minute_str,
                                    time_words[nextHour(h)])

print time_str

