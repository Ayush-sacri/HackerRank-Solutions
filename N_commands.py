def input_loop(z):
    #my_list=["insert","print","remove","append","sort","pop","reverse"]
    empty_list_2=[]   
    empty_list=[]
    empty_list_3=[]
    
    dic={}
    #i=0
    for i  in range(0,z,1):
        user_input=input("enter the command").split()
        x=list(map(int,user_input[1:3]))
       
        
        if user_input[0]=="insert":
            empty_list.insert(x[0],x[1])
        
        
        elif user_input[0]=="remove":
            empty_list.remove(x[0])
            
        elif user_input[0]=="append":
            empty_list.append(x[0])
            
        elif user_input[0]=="sort":
            empty_list.sort()
            
        elif user_input[0]=="pop":
            empty_list.pop()
            
        elif user_input[0]=="reverse":
            empty_list.reverse()
            
        elif user_input[0]=="print":
            empty_list_tiral=[empty_list_2.append(empty_list[j]) for j in range(0,len(empty_list),1)]
            empty_list_3=empty_list_3 + [empty_list_2]
            empty_list_2=[]
            #print(f'empty_list_2= {empty_list_2} empty_list= {empty_list} empty_list_3{empty_list_3}')

            #print(f'empty_list_2= {empty_list_2} empty_list after updation= {empty_list}')
        

        
        
         
    
    #print("empty_list_2 = ",empty_list_2)     
    result=[print(b,end='\n') for b in empty_list_3]
    return (result)






#object creation 
input_element=int(input("enter the number of elements"))
a=input_loop(input_element)
#print(a)
