n=input('Enter a number:')
n=n.lstrip("0")
sum=0
for i in n:
    sum+=int(i)**len(n)   
if sum==int(n):
    print('The number is armstrong')
else:
    print('The number is not armstrong')

    