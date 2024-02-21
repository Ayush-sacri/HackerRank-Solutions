from distutils.command.sdist import sdist


def average(dictionary,find_user,no_elements):
    
    marks=0
    for x in dictionary[find_user]:
        marks=marks+x
    
    average_marks=marks/no_elements
    return  (average_marks)


user_input=int(input("enter how many elemnts"))
user_dict={}
for i in range(0,user_input):
    user_input_elements=input("enter your data ")
    user_input_elements_list=user_input_elements.split()
    user_key=user_input_elements_list[0]
    finding_value=user_input_elements_list[1:len(user_input_elements)+1]
    user_value=list(map(float,finding_value))
    user_dict.update({user_key:user_value})
print("user_dict= ",user_dict)
user_find=input("enter the name of the element you want average for")
user_input_length=float(len(user_dict[user_find]))
getting_vaue=average(user_dict,user_find,user_input_length)
print('averga marks of a number %.2f'%getting_vaue)