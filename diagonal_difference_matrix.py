import sys
import math
import os
import random
import re
import sys
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr,n):
    # Write your code here
    diag=[]
    anti_diag=[]
    for i in range(n):
        anti_diag.append(arr[i][(n-1)-i])
    for i in range(n):
        diag.append(arr[i][i])
    sum_diag=sum(diag)
    sum_anti_diag=sum(anti_diag)
    return(abs(sum_anti_diag-sum_diag))

if __name__ == '__main__':
    n = int(input().strip())
    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    print(arr)
    result = diagonalDifference(arr,n)
    print(result)
sys.exit()
    
