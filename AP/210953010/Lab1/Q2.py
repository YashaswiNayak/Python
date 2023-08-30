n=int(input('Enter the size: '))
x=1
for i in range(0,n):
    for j in range(0,i+1):
         print(x,end=" ")
         x+=1
    print()

