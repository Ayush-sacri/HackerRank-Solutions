import sys
def check_ch(string):
    isalnum=0
    isalpha=0
    isdigit=0
    islower=0
    isupper=0
    user_list=list(string)
    user_len=len(user_list)
    list_1={"isalnum":0,"isalpha":0,"isdigit":0,"islower":0,"isupper":0}
    list_len=len(list_1)
    
    for i in range(user_len): 
        if user_list[i].isalnum()==True:
            list_1["isalnum"]=list_1["isalnum"] +1
        if user_list[i].isalpha()==True:
            list_1["isalpha"]=list_1["isalpha"] + 1
            

        if user_list[i].isdigit()==True:
            list_1["isdigit"]=list_1["isdigit"] + 1    

        if user_list[i].islower()==True:
            list_1["islower"]=list_1["islower"] + 1
    
        if user_list[i].isupper()==True:
            list_1["isupper"]=list_1["isupper"] + 1 
    
    
    for k in list_1:
        if list_1[k]>0:
            print(True)
        else:
            print(False)


        

if __name__ == '__main__':
    s = input()
    check_ch(s)