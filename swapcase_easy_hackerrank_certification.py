user_input1=input("enter the sentence")
user_input_3=user_input1.swapcase()
list1=user_input_3.split()
list1.sort(reverse=True)
for j in list1:
    print(j,end=" ")
         
