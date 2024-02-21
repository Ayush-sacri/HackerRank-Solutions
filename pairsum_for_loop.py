
def pairSum(arr, s):
    # Write your code here.
    empty_list=[]
    
    length_list=len(arr)
    
    for i  in range(0,length_list):
        empty_list_2=[]
        
        #print("value of i ",i)
        for j in range(0,i+1):
            if int(arr[i])+int(arr[j])==int(s):
                empty_list_2.append(int(arr[i]))
                empty_list_2.append(int(arr[j]))
                empty_list_2.sort()
                empty_list.append(empty_list_2)
    empty_list.sort()
    return(empty_list)

def making_string(val):
    for i in val:
        print(" ".join(map(str, i)))
        
    
    

user_list_length_input=input("")  #taking input
user_list_length=user_list_length_input.split() #converting string into list
user_input=input("")#taking list input
user_list_input=user_input.split() 
a=pairSum(user_list_input,user_list_length[1])#passing arguments in pari sum
b=making_string(a)
