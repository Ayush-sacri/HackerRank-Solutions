## palindrome 
def isPalindrome(s: str):
    a=list(s)
    b=list(s)
    b.reverse()
    main_val=b
    if main_val == a:
       return(1)
    else: 
        return(0)
    

empty_list=[]
x=int(input(""))
for i  in range (x):
    empty_list.append(input(""))
    
for j in empty_list:
     print(isPalindrome(j))
        
    
    