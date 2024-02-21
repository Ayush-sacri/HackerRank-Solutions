'''

    Time Complexity: O(N^2)
    Space Complexity: O(1)

    Where 'N' is the size of the array.

'''

def pairSum(s,dict):
    arr=dict["target_val"]
    n = len(dict["target_val"])

    # Used to store result.
    ans = []
    
    # Checking sum for every element.
    for i in range(n):
        
        for j in range(i + 1, n):
            
            if (arr[i] + arr[j] == s):
                pair = [-1 for i in range(2)]
                pair[0] = arr[i]
                pair[1] = arr[j]
                ans.append(pair)

    # Used to store final sorted result.
    res = [[-1 for j in range(2)] for i in range(len(ans))]
    for i in range(len(ans)):
        a = ans[i][0]
        b = ans[i][1]
        res[i][0] = min(a, b)
        res[i][1] = max(a, b)

    res = sorted(res, key=lambda x: x[0])
    #print(res)

    return res

user_input=input("").split()
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
#print("sorted value= ",user_dict)
global a 
a=user_dict["target_val"]
#print(f"value of dict[target] = {a }")
getting_vaue=pairSum(target_val,user_dict)
#print("averga marks of a number",getting_vaue)


for i in getting_vaue:
        print(" ".join(map(str, i)))