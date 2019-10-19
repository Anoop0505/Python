#program_1
p=int(input('Enter the princile amount: '))
t=int(input('Enter the time: '))
r=int(input('Enter the rate: '))
si=p*t*r/100
print('Simple intrest = ',si)



#program_2
p=int(input('Enter the princile amount: '))
t=int(input('Enter the time: '))
r=int(input('Enter the rate: '))
ci=p*(1+r/100)**t
print('Compound intrest = ',ci)




#program_3
c=int(input('Enter the temperature in celsius '))
f=(c*9/5)+32
print('Fahrenheit',f)




#program_4
p=int(input('Enter Pounds'))
i=int(input('Enter Inches'))
k=int(input('Enter Kilometers'))
g=p*453.59
c=i*2.53
m=k*0.6213
print('Pounds to Grams',g)
print('Inches to Centimeters',c)
print('Kilometer to Miles',m)
g=int(input('Enter Grams'))
p=g/453.59
print('Grams to Pounds',p)




#program_5
x=int(input('Enter the values of x '))
y=int(input('Enter the values of y '))
a=x+y
s=x-y
m=x*y
d=x/y
e=x//y
f=x%y
g=x**y
print('{} + {} = '.format(x,y),a)
print('{} - {} = '.format(x,y),s)
print('{} * {} = '.format(x,y),m)
print('{} / {} = '.format(x,y),d)
print('{} // {} = '.format(x,y),e)
print('{} % {} = '.format(x,y),f)
print('{} ** {} = '.format(x,y),g)