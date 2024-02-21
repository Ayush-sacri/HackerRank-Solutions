#matrix ban gaya bhaiii 

row=int(input("enter the number of rows"))
col=int(input("enter the number of columns"))



blank_list2=[]

for i in range(row):
    blank_list1=[]
    print("blank_list1",blank_list1)
    for j in range(col):
        letter=int(input("enter the number"))
        blank_list1.append(letter)
    blank_list2.append(blank_list1)    
print(blank_list2)    
    