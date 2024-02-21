n=int(input("enter the element of a tupple"))
user_elements=(input("enter the elements")).split()
user_integer=list(map(int,user_elements))
t=tuple(user_integer)
#print(t)
hash_value=hash(t)

print(hash_value)