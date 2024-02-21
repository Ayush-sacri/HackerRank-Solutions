def set_function(ele,funx):
    s=set(map(int,ele))
    sum=0
    for k in range(len(funx)):
        if funx[k][0]=='pop':
            s.pop()
            
        elif funx[k][0]=='remove':
            s.remove(int(funx[k][1]))
            
        elif funx[k][0]=='discard':
            s.discard(int(funx[k][1]))
    
    for a in s:
        sum=int(a)+sum
    return(sum)


n = int(input())
elements=input().strip().split()
no_of_funx=int(input())
empty_list=[]
for i in range(no_of_funx):
    ele=input().strip().split()
    empty_list.append(ele)
#print(empty_list)
print(set_function(elements,empty_list))    