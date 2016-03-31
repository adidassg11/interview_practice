#!/bin/python

import sys


time = raw_input().strip()
if time[8] == 'P':
    hour = int(time[:2])
    hour += 12
    time = str(hour) + time[2:]

time = time[:8]
print time
