n=int(input('Enter the lower limit: '))
m=int(input('Enter the upper limit: '))
for i in range(n,m+1):
    prime=True
    for j in range(2,i):
        if i%j==0:
          prime=False
          break
    if prime and i>1:
        print(i)  
        