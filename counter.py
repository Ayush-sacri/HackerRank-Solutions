from collections import Counter
X = input()
x = input().split()
d = dict(Counter(x))
s = 0
for i in range(int(input())):
    key, value = input().split()
    if key in x and d[key] > 0:
        s += int(value)
        d[key] -= 1
print(s)
    
    