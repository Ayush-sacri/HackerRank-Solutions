import sys 
def reverseArray(a,b):
    user_val=a.split()
    #print("user_val",user_val)
    user_val2=user_val[:b+1]
    stored_val=user_val[b+1:]
    stored_val.reverse()
    #print("len of stored val",stored_val)
    for j in range (len(stored_val)):
        user_val2.append(stored_val[j])
        #print(user_val2,"stored value",stored_val)
    return(" ".join(user_val2))
    #return(user_val2)14


class_list ={}
x=int(input("enter the number of test cases "))
for i in range(x):
    class_list1={}
    x=input("enter the data").split()
    data = input('Enter name & score separated by ":" ')
    #temp = data.split(" ")
    class_list1[data] =x[1]
    class_list.update(class_list1)
print("class_list",class_list)
for k in class_list:
    # print(k,class_list[k])
    acc=reverseArray(k,int(class_list[k]))
    print(acc)
sys.exit()