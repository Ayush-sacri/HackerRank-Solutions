# Enter your code here. Read input from STDIN. Print output to STDOU
from itertools import permutations

def function_x(perm,i):
    perm_1=list(permutations(perm,int(i)))
    user=[]
    for k in perm_1:
        a="".join(k)
        user.append(a)
    user.sort()
    for p in user:
        print(p)   
user_input=input().split(" ")
a=function_x(user_input[0],user_input[1])