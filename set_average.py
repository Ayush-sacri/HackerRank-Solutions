def average(array):
    arr_len=len(array)
    set_array=set(array)
    sum_1=0
    c=list(set_array)
    for j in range(0,arr_len-2):
        sum_1=sum_1+ c[j]
    
        
    avg=(sum_1/arr_len)    
    return(avg)

    
    # your code goes here

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)