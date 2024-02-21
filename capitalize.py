def solve(s):
    user_input=s.split(" ")
    word_2=[]
    word_3=""

    for i in range(len(user_input)):
        
        word_1=user_input[i].capitalize()
        word_2.append(word_1)

    return(" ".join(word_2))
    
    

user_input_2=input("entert the name ")
print(solve(user_input_2))
