

from ctypes.wintypes import FLOAT
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

def timeConversion(s,sep):
    # Write your code here
    if s[-2]=='P' and int(sep[0])!=12:
        result_1=12+int(sep[0])
        print("pm")
     
    elif  s[-2]=='P' and int(sep[0])==12:
            result_1=12
    
    elif s[-2]=='A'   and int(sep[0])==12:
        result_1="00"
     
    elif s[-2]=='A'   and int(sep[0])!=12 :
        result_1=sep[0]
    sep[0]=str(result_1)
    a=list(sep[-1])
    a.pop(-1)
    a.pop(-1)
    b="".join(a)
    sep[-1]=b
    print(":".join(sep))
    
if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s_string = input()
    s=list(s_string)
    sep=s_string.split(":")
    result = timeConversion(s,sep)

    #fptr.write(result + '\n')
    #fptr.close()
