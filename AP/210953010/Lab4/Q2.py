import cmath
m=int(input('Enter real part of complex number: '))
n=int(input('Enter imaginary part of complex number: '))
z=complex(m,n)
print('The sine of the value is: ',cmath.sin(z))
print('The square root is: ',cmath.sqrt(z))
print('The log of the number is: ',cmath.log(z))