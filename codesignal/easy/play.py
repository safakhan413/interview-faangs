#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'foo' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER flightDuration
#  2. INTEGER_ARRAY movieDuration
#
# algo:
#  1. calculate td
#  2. iterate through the movieDuration i,v (two for loops for now)
#  3. add each pair and see when it matches td.
# 4. new list, and retunr it with the indices

# diff = td - v
# if diff in md

def foo(fd, md):
    # Write your code herez
    md.sort()
    print(f'im fd {fd}')
    print(f'im md {md}')
    td = fd - 30
    for i, v in md:
        diff = td - v
        if diff not in md: continue
        ind = list()
        ind.append(i, md.find(diff))
        print(f'im ind{ind}')


# if __name__ == '__main__':