def unique(l1:list):
    uniq_lis=[]
    for i in l1:
        if i not in uniq_lis:
            uniq_lis.append(i)
    return uniq_lis
l1=[]
n=int(input("Enter the size of the array"))
print("Enter the array elements")
for i in range(n):
    l1.append(int(input(f'{i+1}: ')))
ans=unique(l1)
print("The list with the unique elements are: ",ans)
