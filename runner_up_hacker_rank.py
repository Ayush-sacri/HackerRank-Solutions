def runner(z):
    z.sort()
    c=max(z)
    i=0
    a=len(z)
    while i!=(a):
        #print("value of i before condition",i)
        if z[i]==c:
            #print(" value of i=",i)
            z.pop(i)
            i=0
            a=a-1 
        
        i=i+1
    print(z[-1])
        
    
    
    
if __name__ == '__main__':
    n = int(input("enter the length of string"))
    arr = list(map(int, input().split()))
    input_list=runner(arr)
    
        