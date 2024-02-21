from itertools import combinations
    string, k = input().split()
    string = ''.join(sorted(string))
    k = int(k)

    result = []
    for i in range(1, k + 1):
        result.extend(list(combinations(string, i)))
    
    for pm in result:
        print(''.join(pm))