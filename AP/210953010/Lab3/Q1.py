def multiply(l1:list):
    product=1
    for i in l1:
        product*=i
    return product
l1=[]
n=int(input("Enter the size of the array"))
print("Enter the array elements")
for i in range(n):
    l1.append(int(input(f'{i+1}: ')))
ans=multiply(l1)
print("The product of all elements of the list is: ",ans)
