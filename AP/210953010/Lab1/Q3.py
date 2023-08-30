n=int(input('Enter the number of strings: '))
l1=[]
for i in range(n):
    l1.append(input())
print('The strings are: ',l1)
count=0
for i in l1:
    if i[0]==i[-1] and len(i)>2:
        count+=1
print('There are',count,' with same first and last characters')
print('The strings with odd length are: ')
for i in l1:
    if len(i)%2!=0:
        print(i)