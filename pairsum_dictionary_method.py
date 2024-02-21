def pairsum(target,dict):
    empty_list=[]
    target_value=int(target)
    sum_value=0
    for x in dict["target_val"]:
       
        if target_value - x in dict["target_val"]:
            print("x",x)
            print("target_value -x ",target_value-x)
            empty_list +=[[x,target_value-x]]
            #if [min(x,target_value-x),max(x,target_value-x)] not in empty_list:
                #empty_list +=[[min(x,target_value-x),max(x,target_value-x)]]
    empty_list_2_len=len(empty_list)
    empty_list_2=[]
    print(f'length of empty_list_2={empty_list_2_len}')
    for i in range(0,(empty_list_2_len//2),1):
        empty_list_2.append(empty_list[i])
        
        
        
    return  (empty_list_2)

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
print("user_dict= ",user_dict)
user_dict["target_val"].sort()
print("sorted value= ",user_dict)
getting_vaue=pairsum(target_val,user_dict)
print("averga marks of a number",getting_vaue)

for i in getting_vaue:
        print(" ".join(map(str, i)))