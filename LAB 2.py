# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 09:12:26 2019

@author: student
"""

#progrma_6
a=int(input('Enter the 1st number:'))
b=int(input('Enter the 2nd number:'))
c=int(input('Enter the 3rd number:'))
d=int(input('Enter the 4st number:'))
e=(a*2**0)+(b*2**1)+(c*2**2)+(d*2**3)
print(e)





#program_7
a=int(input('Enter the hypotenuse'))
b=int(input('Enter the side'))
import math
c=math.sqrt(a**2+b**2)
print(c)





#program_8
y=int(input('Enter the price of the bike'))
x=int(input('Enter the year to be calculated'))
z=y**(x+4)
print('At the year of 5 the price of the bike is ',z)






#program_9
a=int(input('enter the number for 100 notes'))
b=int(input('enter the number for 500 notes'))
c=int(input('enter the number for 2000 notes'))
f=a*100+b*500+c*2000
print('Total amount = ',f)





#program_10
a=int(input('Enter the number:'))
b=int(input('Enter the number: '))
a,b=b,a
print('After swaping a={} and b={}'.format(a,b))




#program_11
a=int(input('Enter the number'))
b=int(input('Enter the number'))
b=a+b
a=b-a
b=b-a
print('the values after swaping ',a,b)






#program_12
a=int(input('a='))
b=1
test=a&b
if(test==0):
     print('Even')
else:
     print('Odd')
     
     


#program13
a=int(input("Enter the value\n"))
b=int(input("Enter the value\n"))
if a is b:
    print("number are equal")
else:
    print("number are not equal")