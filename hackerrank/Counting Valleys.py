#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#################### Algo ###############################
#1. track with variable the position of hiker above or below sea level
# 2. track 0 where next element is


def countingValleys(steps, path):
    aboveOrBelow = 0
    arrAbBelow = []
    timeValley = 0
    for s in path:
        aboveOrBelow = aboveOrBelow + 1 if s == 'U' else aboveOrBelow - 1
        arrAbBelow.append(aboveOrBelow)
    if arrAbBelow[0] != 0: ##because it may start with dd and it would be the 1st valley in that scenario
        arrAbBelow.insert(0,0)
        steps +=1

    print(arrAbBelow)
    for i, aorb in enumerate(arrAbBelow):
        if i != steps -1 and aorb == 0 and (arrAbBelow[i+1] < 0 ):
            timeValley += 1
    return timeValley

s= 'UDDDUDUUDDUU'
steps=12

tv = countingValleys(steps,s)
print(f'time valley {tv}')

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#     steps = int(input().strip())
#
#     path = input()
#
#     result = countingValleys(steps, path)
#
#     fptr.write(str(result) + '\n')
#
#     fptr.close()
