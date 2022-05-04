import math
import os
import random
import re
import sys


#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def print_six_digits(a, size):
    print(f'{a / size:.6f}')


def plusMinus(arr):
    pos, neg, zero = [], [], []
    n = len(arr)
    for i in arr:
        if i > 0:
            pos.append(i)
        elif i < 0:
            neg.append(i)
        else:
            zero.append(i)

    print_six_digits(len(pos), n)
    print_six_digits(len(neg), n)
    print_six_digits(len(zero), n)


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
