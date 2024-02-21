marksheet=[]
marks=[]
x=int(input("enter the list"))
for i in range(x):
    name=input()
    grade=float(input())
    marksheet+=[[name,grade]]
    marks+=[grade]
sl=(sorted(set(marks)))[1]
for i,j in sorted(marksheet):
    if j==sl:
        print(i)

