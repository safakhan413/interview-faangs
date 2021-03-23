import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    list = dict()
    for a in ar:
        print(a)
        list[a] = list.get(a,0)+1
    print(list)
    pair=0
    for k,v in list.items():
        pair += v//2 ##gives quotient
    return pair


ar =[1,2,1,2,1,3,2]
n = 7

pairs = sockMerchant(n,ar)
print(pairs)
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#     n = int(input())
#
#     ar = list(map(int, input().rstrip().split()))
#
#     result = sockMerchant(n, ar)
#
#     fptr.write(str(result) + '\n')
#
#     fptr.close()
