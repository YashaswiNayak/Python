def letters(n:str):
    upper=0
    lower=0
    for i in n:
        if i>='A' and i<='Z':
            upper+=1
        else:
            lower+=1
    print('The number of uppercase letters are: ',upper)
    print('The number of lowercase letters are: ',lower)

x=input("Enter the string")
letters(x)