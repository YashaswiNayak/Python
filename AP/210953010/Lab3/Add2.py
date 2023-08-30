def pascal(n:int):
    for i in range(n+1):
        for j in range(n-i):
            print(end=" ")
        c=1
        for j in range (1,i+1):
            print(c,end=" ")
            c=c*(i-j)//j
        print('\r')
            
n=int(input())
pascal(n)