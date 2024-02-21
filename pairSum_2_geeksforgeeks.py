from ast import Global
from itertools import combinations
def my_pair_sum(S,dict):
    s=int(S)
    count=0
    empty_list=[]
    print("dict",dict["target_val"])
    comb=combinations(dict["target_val"],2)
    for i in comb:
        if sum(i)==s:
            print(i)
            list_a=list(i)
            empty_list.insert(count,list_a)
            count+=1
            
    return empty_list


user_input=input("enter how many elemnts").split()
target_val=int(user_input[1])
user_dict={}
for i in range(0,1):
    user_input_elements=input("enter your data ")
    global user_input_elements_list
    user_input_elements_list=user_input_elements.split()
    finding_value=user_input_elements_list[0:len(user_input_elements)+1]
    user_value=list(map(int,finding_value))
    user_dict.update({"target_val":user_value})
user_dict["target_val"].sort()
print("sorted value= ",user_dict)
global a 
a=user_dict["target_val"]
print(f"value of dict[target] = {a }")
getting_vaue=my_pair_sum(target_val,user_dict)
print("averga marks of a number",getting_vaue)


for i in getting_vaue:
        print(" ".join(map(str, i)))