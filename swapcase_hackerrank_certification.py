user_input1=input("enter the sentence")
user_input=[user_input1[i] for i in range(len(user_input1))]



#print("user_input1",user_input1)
#print("user_input",user_input)
user_length=len(user_input1)
#print("user_length",user_length)
blank_list1=[]


for i in range(0,user_length):
    #print("value of i ",i)
    if user_input[i].islower()==True:
        
        blank_list1.append(user_input[i].upper())
        #print("blank_list",blank_list1)
    
    elif user_input[i].isupper()==True:
        #print("value of i ",i)
        blank_list1.append(user_input[i].lower())
    elif user_input[i]==" ":
        print("value of i",i)
        blank_list1.insert(i," ")
        
a=" "
print("black list1 reverse",blank_list1)    
for x in blank_list1:
    a=a+x  
list1=a.split()
list1.sort(reverse=True)
print("lista ",list1)
for j in list1:
    print(j,end=" ")
         
