def findDuplicate(arr):
    arr.sort()
    user_len=len(arr)
    count=0
    for i in range(user_len):
        if arr[i]==arr[i-1]:
            return(arr[i])


user_input1=0
empty_list=[]
x=int(input("no of test cases "))
for i in range(x):
    user_length=int(input("enter the array size"))
    user_input=input("enter the number").split()
    empty_list.append(list(map(int,user_input)))
for k in empty_list:
    print(findDuplicate(k))

