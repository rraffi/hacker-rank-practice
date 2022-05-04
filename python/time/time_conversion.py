'''
07:05:45PM
hr:mm:ss:mer <- split time at :

'''
# !/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    h = int(s[:2])
    msec = s[2:8]

    hh = h % 12 if s[-2:] == 'AM' else h % 12 + 12

    return f'{hh:02}{msec}'


if __name__ == '__main__':

    s = input()
    result = timeConversion(s)
    print(result)

