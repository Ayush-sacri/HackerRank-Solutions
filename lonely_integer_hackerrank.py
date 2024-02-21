import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    # Write your code here
    a.sort()
    res ={}

    for i in a:
        res[i]=a.count(i)
    
    for i in res:
        if res[i]==1:
            print(i)
    

if __name__ == '__main__':
    n = int(input().rstrip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

