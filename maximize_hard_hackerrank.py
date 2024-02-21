from itertools import product
def functionx(k,M):
    max_ = 0
    for elem in product(*k):
        sum_ = sum(map(lambda x: (x ** 2) % M, elem)) % M
        if sum_ >= max_:
            max_ = sum_
    return max_
k,m=input().split(" ")
empty_list=[]
for i in range(int(k)):
    user_input=input("").strip()[1:].split()
    user_input_1=list(map(int,user_input))
    empty_list.append(user_input_1)
a=functionx(empty_list,int(m))
print(a)