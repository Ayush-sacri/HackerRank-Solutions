# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

def product_list(list_a,list_b):
    a_b_1=[list_a,list_b]
    a_b=list(product(*a_b_1))
    for t in a_b:
        print(t,end=" ")
user_input_a=input("").strip().split(" ")
user_input_a_int=list(map(int,user_input_a))
user_input_b=input("").strip().split(" ")
user_input_b_int=list(map(int,user_input_b))
a=(product_list(user_input_a_int,user_input_b_int))